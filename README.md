# Auto-Reboot-EC2-Instance-on-High-CPU-Load
This project automatically monitors an AWS EC2 instance's CPU utilization. When CPU usage crosses a defined threshold (e.g., 80%), it triggers a Lambda function that programmatically reboots the instance and sends an email notification via AWS SNS.

🚀 Architecture
AWS EC2: Instance that is monitored.

AWS CloudWatch: Watches the CPUUtilization metric and triggers alarms.

AWS Lambda: Automatically reboots the instance when CPU is high and sends a notification.

AWS SNS (Simple Notification Service): Sends an email to alert that the instance was rebooted.

IAM Role: Provides Lambda with permissions to manage EC2 and publish to SNS.

🔥 How It Works
CloudWatch Alarm monitors EC2 CPUUtilization.

When CPU > 80% (or a set threshold), CloudWatch triggers the Lambda function.

Lambda reboots the EC2 instance using reboot_instances() API.

Lambda then publishes a message to an SNS Topic notifying about the reboot action.

SNS sends an email alert to the subscribed user.

📂 Technologies Used
AWS EC2

AWS CloudWatch

AWS Lambda (Python 3.12)

AWS SNS

IAM Roles and Policies

📜 Future Enhancements
Add condition in Lambda to check instance status before rebooting.

Reboot only specific EC2 tags (example: only reboot "production" servers).

Improve Lambda error handling and retries.

Integrate Slack/Webhook notifications instead of only email.

Add automatic scaling actions instead of just rebooting.

✨ Learning Outcomes
Hands-on experience with AWS event-driven services.

Practical understanding of Lambda triggers and SNS integration.

Importance of auto-healing systems for Cloud Support roles (like AWS CSA).

How to monitor metrics and take actions without human intervention.

📌 This project is highly relevant for Cloud Support Associate (CSA) interviews and demonstrates automation, monitoring, and operational excellence using AWS.
