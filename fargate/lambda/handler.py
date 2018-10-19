import boto3

def handler(event, context):
    cluster = 'your_cluster_name'
    task = 'ec-compute-fargate-dev'
    client = boto3.client('ecs', region_name='us-east-1')

    response = client.run_task(
        cluster=cluster,
        launchType='FARGATE',
        taskDefinition=task,
        count=1,
        platformVersion='LATEST',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'subnet-',      # <- setup your aws account vpc
                    'subnet-'
                ],
                "securityGroups": [
                    'sg-'
                ],
                'assignPublicIp': 'ENABLED'
            }
        }
    )
    print(response)
    
# print(handler(None, None))