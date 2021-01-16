#this code creates an ec2
import boto3
ec2 =  boto3.client('ec2')
ec2.run_instances(ImageId='ami-0be2609ba883822ec', InstanceType='t2.micro', SubnetId='subnet-07469a71c283170ae', MinCount=1, MaxCount=1)
