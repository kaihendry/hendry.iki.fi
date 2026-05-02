INFILES = $(shell find . -name "*.src.html")
OUTFILES = $(INFILES:.src.html=.html)
SC := "REDUCED_REDUNDANCY"

all: $(OUTFILES)

FEEDGEN = ./feedgen -link "$(1)" '$(2)' > $@.tmp && mv $@.tmp $@ || (rm -f $@.tmp && echo '<!-- feed unavailable -->' > $@)

youtube.inc:
	$(call FEEDGEN,https://www.youtube.com/user/kaihendry?sub_confirmation=1,https://www.youtube.com/feeds/videos.xml?channel_id=UCFzGyNKXPAglNq28qWYTDFA)

youtube2.inc:
	$(call FEEDGEN,https://www.youtube.com/channel/UCE5Au4LfcBHxTQR_yLbncrQ?sub_confirmation=1,https://www.youtube.com/feeds/videos.xml?channel_id=UCE5Au4LfcBHxTQR_yLbncrQ)

natalian.inc:
	$(call FEEDGEN,https://natalian.org/,http://natalian.org/index.rss)

dabase.inc:
	$(call FEEDGEN,https://dabase.com,https://dabase.com/blog/index.xml)

%.html: %.src.html youtube.inc youtube2.inc natalian.inc dabase.inc
	@m4 -PEIinc $< > $@
	@echo $< →  $@

upload: index.html
	@aws s3 sync --delete --storage-class ${SC} \
		--acl public-read \
		--exclude "*.src.html" \
		--exclude '*.git/*' \
		. s3://hendry.iki.fi/
	@echo Uploaded to http://hendry.iki.fi.s3-website-ap-southeast-1.amazonaws.com/
	@aws cloudfront create-invalidation --distribution-id E1SYBAHZYXXHGM --invalidation-batch "{ \"Paths\": { \"Quantity\": 1, \"Items\": [ \"/*\" ] }, \"CallerReference\": \"$(shell date +%s)\" }"

clean:
	rm -f index.html *.inc
