import os
import boto3
from datetime import datetime, date
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')


def upload_to_s3(local_file, bucket, object_name=None, prefix=None):
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN
    )

    s3 = session.client('s3')

    s3_file_path = f'raw_zone/b3/{date.today()}/b3_{str(datetime.now()).replace(' ','_')}.parquet'

    try:
        s3.upload_file(local_file, bucket, s3_file_path)
        print(f"Upload Successful: {s3_file_path}")
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
