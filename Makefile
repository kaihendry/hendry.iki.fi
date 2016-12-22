all:
	@aws s3 sync --storage-class STANDARD_IA --acl public-read . s3://hendry.iki.fi/
	#@aws cloudfront create-invalidation --distribution-id E2AXSD6P2TRMEA --invalidation-batch "{ \"Paths\": { \"Quantity\": 1, \"Items\": [ \"/*\" ] }, \"CallerReference\": \"$(shell date +%s)\" }"
