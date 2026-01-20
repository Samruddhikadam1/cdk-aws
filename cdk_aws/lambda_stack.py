from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_s3 as s3,
    aws_kms as kms
    # aws_sqs as sqs,
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, bucket: s3.IBucket, kms_key: kms.IKey, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3_get_role = iam.Role(
            self,
            "S3GetRole",
            role_name="S3GetRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )
        s3_get_role.add_to_policy(
            iam.PolicyStatement(
                actions=["s3:ListBucket"],
                resources=[bucket.bucket_arn]
            )
        )

        s3_get_role.add_to_policy(
            iam.PolicyStatement(
                actions=["s3:GetObject"],
                resources=[f"{bucket.bucket_arn}/*"]
            )
        )

        s3_get_role.add_to_policy(
            iam.PolicyStatement(
                actions=[
                    "kms:Decrypt",
                    "kms:DescribeKey"
                ],
                resources=[kms_key.key_arn]
            )
        )

        _lambda.Function(
            self, "MyLambda",
            function_name="MyLambda07",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="handler.handler",
            code=_lambda.Code.from_asset("lambda"),
            role=s3_get_role
        )
