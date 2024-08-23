provider "aws" {
  region = "us-east-1"
}

resource "aws_dynamodb_table" "examy_dynamedb_table" {
  name         = "example-table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }

  server_side_encryption {
    enabled     = true
    kms_key_arn = "arn:aws:kms:us-west-2:123456789012:key/KMS-key-id"
  }
}
