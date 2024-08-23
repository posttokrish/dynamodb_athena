package aws.dynamodb.test

import data.aws.dynamodb

test_dynamodb_encryption_compliance {
  not dynamodb.deny
}

test_dynamodb_encryption_non_compliance {
  some msg
  msg := dynamodb.deny[_]
}

