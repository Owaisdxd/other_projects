import boto3

region='ap-northeast-1' #Change it as per your desired region

s3= boto3.client('s3',region_name=region)

bucket_name='MyFirstBucket'


response=s3.create_bucket(
        Bucket=bucket_name, 
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
)

print(response)
