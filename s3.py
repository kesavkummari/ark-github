import boto3
import botocore

def create_s3_bucket(bucket_name, region="us-east-1"):
    try:
        s3_client = boto3.client("s3", region_name=region)

        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )

        print(f"✅ S3 bucket '{bucket_name}' created successfully in {region}.")

    except botocore.exceptions.ClientError as error:
        print(f"❌ Error creating bucket: {error}")

if __name__ == "__main__":
    bucket_name = "my-unique-bucket-name-12345"  # Change to a globally unique name
    region = "us-east-1"  # Change region if needed
    create_s3_bucket(bucket_name, region)
