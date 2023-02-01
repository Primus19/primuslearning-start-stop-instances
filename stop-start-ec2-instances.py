import boto3
region = 'us-east-1'
instances = ['ReplaceinstanceID'] 
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
   # ec2.stop_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
    #print('stopped your instances: ' + str(instances))