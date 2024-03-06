import boto3

instance_id = ''
ec2 = boto3.resource('ec2')
instance = ec2.Instance(instance_id)

