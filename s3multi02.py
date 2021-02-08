import boto3, time
from boto3.s3.transfer import TransferConfig

MB = 1024
config = TransferConfig(multipart_threshold=10*MB,
                        max_concurrency=10,
                        multipart_chunksize=5*MB,
                        use_threads=True)

S3_BUCKET = 'java-web-sample-war'
FILE_PATH = 'D:\\tmp\\Lectures.7z'
KEY_PATH = "Lectures.7z"

def ProgressPercentage (file):
	print(file)

t1 = time.time()
# Perform the transfer
s3 = boto3.client('s3')
res  = s3.upload_file(FILE_PATH, S3_BUCKET, KEY_PATH,
               Config=config,
               Callback=ProgressPercentage(FILE_PATH))
t2 = time.time()
print("Time taken: {0:.3f} seconds" .format(t2-t1))
print(res)