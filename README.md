# Auto-Reboot-EC2-Instance-on-High-CPU-Load
This project automatically monitors an AWS EC2 instance's CPU utilization. When CPU usage crosses a defined threshold (e.g., 80%), it triggers a Lambda function that programmatically reboots the instance and sends an email notification via AWS SNS.
