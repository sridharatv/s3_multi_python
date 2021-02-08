import boto3
from boto3.s3.transfer import TransferConfig

s3_client = boto3.client('s3')

S3_BUCKET = 'demo-bucket-aug-2020'
FILE_PATH = 'D:\\tmp\\'
KEY_PATH = ""

def ProgressPercentage (file):
    print(file)

def uploadFileS3(filename):
    config = TransferConfig(multipart_threshold=1024*5,
                            max_concurrency=4,
                            multipart_chunksize=1024*5,
                            use_threads=True)
    file = FILE_PATH + filename
    key = KEY_PATH + filename
    s3_client.upload_file(file, S3_BUCKET, key,
    ExtraArgs={ 'ACL': 'public-read', 'ContentType': 'application/java-archive'},
    Config = config,
    Callback=ProgressPercentage(file)
    )

uploadFileS3('WordCount.jar')