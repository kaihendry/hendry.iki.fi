SC := "REDUCED_REDUNDANCY"
all:
	@aws s3 sync --delete --storage-class ${SC} --acl public-read --exclude '*.git/*' . s3://hendry.iki.fi/
	@aws s3 cp --storage-class ${SC} --acl public-read --cache-control="max-age=86400" kaihendry.svg s3://hendry.iki.fi/
	@echo Uploaded to http://hendry.iki.fi.s3-website-ap-southeast-1.amazonaws.com/
	#@aws cloudfront create-invalidation --distribution-id E1SYBAHZYXXHGM --invalidation-batch "{ \"Paths\": { \"Quantity\": 1, \"Items\": [ \"/*\" ] }, \"CallerReference\": \"$(shell date +%s)\" }"
