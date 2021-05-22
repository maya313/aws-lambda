import json
import boto3

def lambda_handler(event, context):
    print(event)
    
    s3 = boto3.resource('s3')
    
    for row in event['Records']:
        bucket_name = row['s3']['bucket']['name']
        bucket_object = row['s3']['object']['key']
        print(bucket_name)
        print(bucket_object)