import boto3
# Initialize the RDS client
rds_client = boto3.client('rds')
#Defining the parameters for your RDS instance
db_instance_name = 'rds'
db_instance_class = 'db.t3.micro'
engine = 'mysql'
master_username = 'owais_ahmed'
masterpassword = 'owais12345!'

#Create the RDS instance
response = rds_client.create_db_instance(
        DBInstanceIdentifier=db_instance_name,
        DBInstanceClass=db_instance_class,
        Engine=engine,
        MasterUsername=master_username,
        MasterUserPassword=masterpassword,
        AllocatedStorage=20, #Specify the storage size in GB
        MultiAZ=False, #Set to True for Multi-AZ deployment
        #Other parameters like VPC security groups, subnet groups, etc.
)

#Checking the response for errors
if 'DBInstance' in response:
    print(f"RDS instance '{db_instance_name}'created successfully")
else:
    print("Error creating RDS instance:", response)

