INFILES = $(shell find . -name "*.src.html")
OUTFILES = $(INFILES:.src.html=.html)
SC := "REDUCED_REDUNDANCY"

all: $(OUTFILES)

youtube.inc:
	node index.js youtube 'https://www.youtube.com/feeds/videos.xml?channel_id=UCFzGyNKXPAglNq28qWYTDFA' > $@

youtube2.inc:
	node index.js youtube2 'https://www.youtube.com/feeds/videos.xml?channel_id=UCE5Au4LfcBHxTQR_yLbncrQ' > $@

natalian.inc:
	node index.js natalian 'http://natalian.org/index.rss' > $@

dabase.inc:
	node index.js dabase 'https://dabase.com/blog/index.xml' > $@

%.html: %.src.html youtube.inc youtube2.inc natalian.inc dabase.inc
	@m4 -PEIinc $< > $@
	@echo $< →  $@

upload: index.html
	@aws configure set preview.cloudfront true
	@aws --profile mine s3 sync --delete --storage-class ${SC} \
		--acl public-read \
		--exclude "node_modules/*" \
		--exclude "*.src.html" \
		--exclude '*.git/*' \
		. s3://hendry.iki.fi/
	@echo Uploaded to http://hendry.iki.fi.s3-website-ap-southeast-1.amazonaws.com/
	@aws --profile mine cloudfront create-invalidation --distribution-id E1SYBAHZYXXHGM --invalidation-batch "{ \"Paths\": { \"Quantity\": 1, \"Items\": [ \"/*\" ] }, \"CallerReference\": \"$(shell date +%s)\" }"

clean:
	rm -f index.html *.inc
