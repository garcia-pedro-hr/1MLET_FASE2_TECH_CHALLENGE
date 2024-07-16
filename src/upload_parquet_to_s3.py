import os
from src.data_processing.data_scrapper import scrape_b3_data
from src.data_processing.data_uploader import upload_to_s3


AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

if __name__ == "__main__":
    local_file = scrape_b3_data()
    uploaded = upload_to_s3(local_file, AWS_BUCKET_NAME)
