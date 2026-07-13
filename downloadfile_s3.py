import boto3

region='ap-northeast-1' #Change it as per your desired region
s3= boto3.client('s3',region_name=region)

bucket_name='bucketname'
local_file='file1_s3.txt'
object_name='file2.txt'

response=s3.download_file(bucket_name, object_name, local_file)

print(response)
