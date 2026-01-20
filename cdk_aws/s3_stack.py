from aws_cdk import (
    aws_s3 as s3,
    Stack
)
from aws_cdk import aws_kms as kms
from constructs import Construct

class S3Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        kms_key = kms.Key(
            self,
            "MyBucketKey",
            enable_key_rotation=True
        )

        bucket = s3.Bucket(
            self,
            "storage-bucket",
            bucket_name="storage-bucket-0704",
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.KMS,
            encryption_key=kms_key
        )

        self.bucket=bucket
        self.kms_key = kms_key
      
