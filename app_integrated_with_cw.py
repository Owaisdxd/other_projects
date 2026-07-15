from flask import Flask
import logging 
import boto3
from botocore.exceptions import NoCredentialsError
import time

app = Flask(__name__)

LOGGING_FORMAT = '%(asctime)s - %(levelname)s -%(message)s' #timestap, log level, actual log
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT) #logging module configuration
logger = logging.getLogger() #create instance

logs = boto3.client('logs', region_name='us-east-1')

def push_to_cw(log_group, log_stream, message):
    try:
        logs.create_log_group(logGroupName=log_group)
    except logs.exceptions.ResourceAlreadyExistsException:
        pass

    try:
        logs.create_log_stream(
                logGroupName=log_group,
                logStreamName=log_stream
        )
    except logs.exceptions.ResourceAlreadyExistsException:
        pass

    timestamp = int(time.time() * 1000)
    logs.put_log_events(
            logGroupName=log_group,
            logStreamName=log_stream,
            logEvents=[
                {
                    'timestamp': timestamp,
                    'message': message
                    },
                ]
            )

@app.route('/')
def hello():
    logger.debug("ok,endpoint hit!")
    push_to_cw("pythonFlaskLogs","FlaskEndpointLogs","ok,endpoint hits!!")
    return "Hello, World!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

