import os
import boto3
from dotenv import load_dotenv
load_dotenv()

username = ''
password = ''

client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))
response = client.initiate_auth(
    ClientId=os.getenv('COGNITO_USER_CLIENT_ID'),
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': username,
        'PASSWORD': password
    }
)

print(response)