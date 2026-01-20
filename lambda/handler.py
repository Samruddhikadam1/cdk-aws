import boto3
import json

s3 = boto3.client("s3")

def handler(event, context):
    bucket_name = "storage-bucket-0704"

    if not bucket_name:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Bucket name not provided"})
        }

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        files = []
        if "Contents" in response:
            for obj in response["Contents"]:
                key = obj["Key"]

                # Fetch file content
                file_obj = s3.get_object(Bucket=bucket_name, Key=key)
                file_body = file_obj["Body"].read().decode("utf-8")

                files.append({
                    "filename": key,
                    "body": file_body
                })

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
