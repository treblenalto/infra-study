import boto3
import time


client = boto3.client("sso", region_name="ap-northeast-3")

s3 = boto3.client("s3")
bucket_name = "hasan-assignment"

# upload files to s3 bucket
start = time.time()
for i in range(1, 101):
    file_name = f"taehee-s3/submission_{i}.csv"
    s3.upload_file("submission.csv", bucket_name, file_name)
end = time.time()
print(f"Upload files to s3 bucket: {end - start} seconds")
print(f"Upload files to s3 bucket: {(end - start) / 100} seconds per file")

# download files from s3 bucket
start = time.time()
for i in range(1, 101):
    file_name = f"submission_{i}.csv"
    s3.download_file(bucket_name, f"taehee-s3/{file_name}", f"s3/{file_name}")
end = time.time()
print(f"Download files from s3 bucket: {end - start} seconds")
print(f"Download files from s3 bucket: {(end - start) / 100} seconds per file")
