import boto3
import json

s3 = boto3.client("s3")

def handler(event, context):
    bucket_name = event.get("bucket")

    if not bucket_name:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Bucket name not provided"})
        }

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        files = []
        if "Contents" in response:
            files = [obj["Key"] for obj in response["Contents"]]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "bucket": bucket_name,
                "files": files
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
