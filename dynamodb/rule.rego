package aws.dynamodb

# Deny rule checks for KMS encryption
deny[msg] {
  input.request.operation == "CreateTable"
  not input.request.payload.SSESpecification.Enabled
  msg := "DynamoDB table must be encrypted with AWS KMS."
}

deny[msg] {
  input.request.operation == "CreateTable"
  input.request.payload.SSESpecification.KMSMasterKeyId == ""
  msg := "A KMS Key ID must be specified for DynamoDB table encryption."
}
