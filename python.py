#!/usr/bin/python3
# listing s3 buckets 
import boto3 
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)


data = open('/tmp/test', 'rb')

s3.Bucket('monolithapp').put_object(Key='/tmp/test', Body=data)