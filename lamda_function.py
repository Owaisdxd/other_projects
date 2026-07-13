def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello, World!'
    }


#Step2: Create a Deployment Package

# Create a directory for your deployment package
mkdir my_lambda_package
cd my_lambda_package

# Copy your Lambda function code to the directory
cp /lambda_function.py .

# Zip the deployment package
zip -r my_lambda_function.zip .


#Step3: Create an IAM Role

aws iam create-role \
    --role-name MyLambdaRole \
    --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}]}'

#Step4:  Attach Permissions to the IAM Role

aws iam attach-role-policy \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole \
    --role-name MyLambdaRole

#Step5: Create the Lambda Function

aws lambda create-function \
    --function-name <your-function-name> \
    --runtime python3.8 \
    --role arn:aws:iam::123456789012:role/MyLambdaRole \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://<path-to-zip-file>

#Step6:
#aws lambda invoke --function-name <your-function-name> output.txt

