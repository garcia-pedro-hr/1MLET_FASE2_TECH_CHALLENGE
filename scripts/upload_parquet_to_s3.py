import os

from src.data_processing.data_scraper import scrape_b3_data
from src.data_processing.data_uploader import upload_to_aws

if __name__ == "__main__":
    local_file = scrape_b3_data()
    bucket_name = os.getenv('BUCKET_NAME')
    s3_file_path = os.getenv('S3_FILE_PATH')
    acess_key = os.getenv('ACESS_KEY')
    secret_key = os.getenv('SECRET_KEY')

    uploaded = upload_to_aws(local_file, bucket_name, s3_file_path, acess_key, secret_key)

    if uploaded:
        print("File uploaded successfully")
    else:
        print("File upload failed")
