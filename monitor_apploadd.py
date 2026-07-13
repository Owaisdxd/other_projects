from selenium import webdriver
import time
import boto3

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the webpage you want to monitor
driver.get("https://practicetestautomation.com/practice-test-login/")

# Measure page load time
start_time = time.time()
driver.get("https://practicetestautomation.com/practice-test-login/")
end_time = time.time()
load_time = end_time - start_time

cloudwatch = boto3.client('cloudwatch')
# Push the metric to CloudWatch
cloudwatch.put_metric_data(
    Namespace='WebPerformance',
    MetricData=[
        {
            'MetricName': 'PageLoadTime',
            'Value': load_time,
            'Unit': 'Seconds',
            'Dimensions': [
                {
                    'Name': 'WebPage',
                    'Value': 'example.com'
                },
            ]
        },
    ]
)

# Close the browser
driver.quit()
