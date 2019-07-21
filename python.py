#!/usr/bin/python3
# listing s3 buckets 
import boto3 
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)


data = open('test', 'rb')

s3.Bucket('monolithapp').put_object(Key='test', Body=data)