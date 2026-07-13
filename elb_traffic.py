import boto3
from datetime import datetime, timedelta

cw=boto3.client('cloudwatch')

elb_name='flaskElb'

end_time=datetime.now()
start_time=end_time - timedelta(days=1)
metric_name='RequestCount'
dimensions=[
        {
            'Name': 'LoadBalancerName',
            'Value': elb_name
        },
]

response=cw.get_metric_data(
       MetricDataQueries=[
            {
                'Id': 'm1',
                'MetricStat': {
                'Metric': {
                     'Namespace': 'AWS/ELB',
                     'MetricName': metric_name,
                     'Dimensions': dimensions
                },
                'Period': 300, # Adjust the periodas needed (in seconds)
                'Stat': 'Sum', # Change to other stats like "Average', "Maximum', etc.
            },
            'ReturnData': True,
        },
    ],

        StartTime=start_time,
        EndTime=end_time,
)

#Print the metric data
print("Metric Data:", response[ 'MetricDataResults'])
for datapoint in response.get('Datapoints', []):
    print(f"Time: {datapoint['Timestamp']}, Request Count: {datapoint[statistic]}")
