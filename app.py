#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk import Environment
from cdk_aws.cdk_aws_stack import CdkAwsStack
from cdk_aws.s3_stack import S3Stack
from cdk_aws.lambda_stack import LambdaStack
from cdk_aws.apigateway_stack import ApiStack

env = Environment(
    account="844216228372",
    region="ap-south-1"
)

app = cdk.App()

CdkAwsStack(app, "CdkAwsStack", env=env)

s3_stack = S3Stack(app, "S3Stack", env=env)

lambda_stack = LambdaStack(app, "LambdaStack", bucket=s3_stack.bucket, env=env)

apigateway_stack = ApiStack(app,"ApiStack", env=env)

app.synth()
