#!/usr/bin/python3
# listing s3 buckets 
import boto3 
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)


data = open('test', 'rb')

# Key is the name of the file that  goes into s3, and the data is the content
# monolitapp is the bucketname
s3.Bucket('monolithapp').put_object(Key='test_2', Body=data)