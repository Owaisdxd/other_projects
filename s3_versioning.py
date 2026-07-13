import boto3

region='ap-northeast-1' #Change it as per your desired region

s3= boto3.client('s3',region_name=region)

bucket_name='MyfirstBucket'


response=s3.put_bucket_versioning(
        Bucket=bucket_name, 
        VersioningConfiguration={
            'Status': 'Enabled'
        }
)

print(response)
