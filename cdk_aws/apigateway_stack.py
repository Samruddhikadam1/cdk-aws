from aws_cdk import (
    Stack,
    aws_apigatewayv2 as apigwv2,
    aws_lambda as _lambda,
    aws_ssm as ssm
)
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration
from constructs import Construct


class ApiStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        #  Create HTTP API
        http_api = apigwv2.HttpApi(
            self,
            "NetworkHttpApi",
            api_name="NetworkHttpApi"
        )

        # Import EXISTING Lambda by FUNCTION NAME (no ARN)
        status_lambda = _lambda.Function.from_function_name(
            self,
            "ImportedStatusLambda",
            "MyLambda07"   # <-- Lambda name created by your friend
        )

        #  Add /status route → existing Lambda
        http_api.add_routes(
            path="/status",
            methods=[apigwv2.HttpMethod.GET],
            integration=HttpLambdaIntegration(
                "StatusIntegration",
                status_lambda
            )
        )

        # Store API base URL in SSM
        ssm.StringParameter(
            self,
            "HttpApiUrlParameter",
            parameter_name="/network/http-api/url",
            string_value=http_api.url
        )
