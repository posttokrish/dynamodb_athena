1) To validate DynamoDB with opa repo rueles
2) Config rule for Athena worg group


1) Dynamodb
  Create a JSON formatted file by
	terraform plan -out=tfplan.binary
	terraform show -json tfplan.binary > plan.json
Then run policy as
	opa eval --input plan.json --data policy.rego 'data.terraform.deny'

2) Athena Workgroup:
iCreate lambda Funcrion
	zip lambda_function.zip lambda_function.py
	terraform plan
	terraform apply
