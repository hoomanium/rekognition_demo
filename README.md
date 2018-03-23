# Amazon Rekognition Text Detection
Using a Rasbperry Pi 3.0 and Pi Camera Module to send images to Amazon Rekognition for text detection.

Disclaimer:
This Python script is only for demonstration purposes and should NOT be used for any other purposes, or shared without explicit permission from the author.

You are fully responsible for the setup, and using and running this script.

# Demo Setup: 

## Hardware
- [Raspberry Pi 3.0](http://a.co/dFSQNyF)
- [Raspberry Pi Camera Module V2](http://a.co/i7atlm4)

## Configuration
1. [Setup Raspberry Pi](https://www.raspberrypi.org/documentation/)
2. [Install Raspberry Pi Camera](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)
4. [Install AWS CLI on Raspberry Pi](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-linux.html)
5. [Install AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/)
5. [Configure AWS CLI with your Security Credentials and Region](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
6. [Create an Amazon S3 Bucket to store images uploaded from Raspberry Pi ](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
7. Download rekognition_demo.py which contains the Python script that I made for this demo on the Raspberry Pi
8. Open rekognition_demo.py with a text editor:
...8.1. Change the variable aws_region to the region you set in step 5 
...8.2. Change the variable bucket_name to the name of the S3 bucket created in step 6.
...8.3. Save the changes and close the file.
9. Run rekognition_demo.py script from terminal using the command: python rekognition_demo.py

