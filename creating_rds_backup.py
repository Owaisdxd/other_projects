#Creating a manul backup of the RDS instance
import boto3

#Initialize the RDS client
rds_client = boto3.client('rds')

backup_name = 'rdsbackup'
db_instance_name = 'rds'

response = rds_client.create_db_snapshot(
        DBSnapshotIdentifier=backup_name,
        DBInstanceIdentifier=db_instance_name
)

#checking the response for errors
if 'DBSnapshot' in response:
    print(f"Manual backup '{backup_name}' created successfully")
else:
    print("Error Creating manual backup:", response)

