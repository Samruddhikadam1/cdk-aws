from aws_cdk import (
    aws_s3 as s3,
    Stack
)
from constructs import Construct

class S3Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self,
            "storage-bucket",
            bucket_name="storage-bucket-07",
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )

        self.bucket=bucket
      
