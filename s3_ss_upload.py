import boto3
from selenium import webdriver
import time

region='your-az' #Change it as per your desired region
s3= boto3.client('s3',region_name=region)
bucket_name='youbucketname' #Should be unique
response=s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': region})
print(response)
driver=webdriver.Chrome()
driver.get("https://aws.amazon.com")
driver.save_screenshot("screenshot_test.png")
object_name="screenshot_test.png"
s3.upload_file(object_name,bucket_name,object_name)
time.sleep(5)
driver.quit()


