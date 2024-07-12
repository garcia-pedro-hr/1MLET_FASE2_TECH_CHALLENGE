import boto3
from botocore.exceptions import NoCredentialsError, ClientError


def upload_to_aws(local_file, bucket, s3_file, acess_key, secret_key, object_name=None, prefix=None):

    session = boto3.Session(
        aws_access_key_id=acess_key,
        aws_secret_access_key=secret_key
    )

    s3 = session.client('s3')

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print(f"Upload Successful: {s3_file}")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except ClientError as e:
        print(f"Client error: {e}")
        return False
