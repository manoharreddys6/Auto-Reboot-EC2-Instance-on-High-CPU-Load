import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')

    instance_id = 'i-0e835860a5a4dde49'  # Your EC2 instance ID
    topic_arn = 'arn:aws:sns:ap-south-1:183295413673:EC2HighCPURebootNotification'  # Your SNS topic ARN

    # Reboot the instance
    response = ec2.reboot_instances(InstanceIds=[instance_id])
    print(f"Reboot initiated for instance {instance_id}. Response: {response}")

    # Publish a notification to SNS
    message = f"CPU usage for EC2 instance {instance_id} crossed the threshold. The instance is being rebooted."
    subject = f"Rebooting EC2 Instance: {instance_id} Due to High CPU Usage"

    sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject
    )
