import boto3
import botocore
import os
BUCKET_NAME = 'mus1307' # replace with your bucket name
KEY = 'awsui.py' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'awsui.py')

except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

import awsui.py

