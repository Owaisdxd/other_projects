import boto3

region='ap-northeast-1' #Change it as per your desired region
s3= boto3.client('s3',region_name=region)

bucket_name='bucketname'
local_file='file1.txt'
object_name='file3.txt'

s3.upload_file(local_file, bucket_name, object_name)
