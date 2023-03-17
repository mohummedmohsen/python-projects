import boto3 

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
        print(f"instance {instance['InstanceId']} is {instance['State']['Name']}")

statuses =  ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    instance_status = status['InstanceStatus']['Status']
    system_status = status['SystemStatus']['Status']
    print(f"Instance {status['InstanceId']} status is {instance_status} and system status is {system_status}")