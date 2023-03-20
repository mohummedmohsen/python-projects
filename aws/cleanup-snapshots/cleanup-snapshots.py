import boto3 
import schedule
from operator import itemgetter

ec2_client = boto3.client('ec2')


snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self']
)

print(snapshots['Snapshots'])

sorted_snapshots = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

for snapshot in sorted_snapshots[2:]:
    response = ec2_client.delete_snapshot(
        SnapshotId=snapshot['SnapshotId']
    )
    
    print(response)

