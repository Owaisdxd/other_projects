import boto3

region='ap-northeast-1' #Change it as per your desired region

s3= boto3.client('s3',region_name=region)

bucket_name='MyFirstBucket'


response=s3.list_object_versions(Bucket=bucket_name)
for version in response.get('Version', []):
    print(f"Object key: {version['Key']}, Version ID: {version['VersionId']}")
