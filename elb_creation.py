import boto3

#Initialize a boto3 client for ELBv2

client=boto3.client('elbv2')

def create_application_load_balancer(name, subnet):
    response=client.create_load_balancer(
            Name=name,
            Subnets=subnet,
            Type='application'
        )
    return response

#Example Usage
#Replace 'Your_subnet_1' , 'Your_subnet_2' with your actual subnet IDS

lb_name='flaskElb'
subnets_list=['subnet_id','subnet_id2']
response=create_application_load_balancer(lb_name,subnets_list)
print(response['LoadBalancers'][0]['LoadBalancerArn'])

