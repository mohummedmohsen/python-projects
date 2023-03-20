import boto3 
import schedule

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

def check_instance_status():
    reservations = ec2_client.describe_instances()
    for reservation in reservations['Reservations']:
        instances = reservation['Instances']
        for instance in instances:
            print(f"instance {instance['InstanceId']} is {instance['State']['Name']}")

    statuses =  ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        instance_status = status['InstanceStatus']['Status']
        system_status = status['SystemStatus']['Status']
        print(f"Instance {status['InstanceId']} status is {instance_status} and system status is {system_status}")
    print("-------------------------------\n")

schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()
