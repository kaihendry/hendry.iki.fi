INFILES = $(shell find . -name "*.src.html")
OUTFILES = $(INFILES:.src.html=.html)
SC := "REDUCED_REDUNDANCY"

all: $(OUTFILES)

youtube.inc:
	node index.js youtube 'https://www.youtube.com/feeds/videos.xml?channel_id=UCFzGyNKXPAglNq28qWYTDFA' > youtube.inc

youtube2.inc:
	node index.js youtube2 'https://www.youtube.com/feeds/videos.xml?channel_id=UCE5Au4LfcBHxTQR_yLbncrQ' > youtube2.inc

%.html: %.src.html youtube.inc youtube2.inc
	@m4 -PEIinc $< > $@
	@echo $< →  $@

upload: index.html
	@aws configure set preview.cloudfront true
	@aws s3 sync --delete --storage-class ${SC} --acl public-read --exclude "node_modules/*" --exclude '*.git/*' . s3://hendry.iki.fi/
	@echo Uploaded to http://hendry.iki.fi.s3-website-ap-southeast-1.amazonaws.com/
	@aws cloudfront create-invalidation --distribution-id E1SYBAHZYXXHGM --invalidation-batch "{ \"Paths\": { \"Quantity\": 1, \"Items\": [ \"/*\" ] }, \"CallerReference\": \"$(shell date +%s)\" }"

clean:
	rm -f index.html *.inc
