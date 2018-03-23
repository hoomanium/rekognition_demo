##########################################################
#    				 			 #
# File name: rekognition_demo.py   		   	 #
# Author:    Hooman Hejazi         		   	 #
# Date:      March 22, 2018        		         #
# Disclaimer:                      		         #
# This Python script is only for demonstration purposes  # 
# and should NOT be used for any other purposes, or 	 #
# shared without explicit permission from the author.    #
#    				 			 #
##########################################################

import boto3
import time
import os
import sys
import picamera
import subprocess
from tempfile import gettempdir
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing


# Globals
camera = picamera.PiCamera()
bucket_name = ""
aws_region = ""
filename = "rekognition_pic00.png"

# S3 Upload Function
def uploadImage():
	# Create an S3 client
	s3 = boto3.client('s3')

	# Uploads the given file using a managed uploader, which will split up large
	# files automatically and upload parts in parallel.
	s3.upload_file(filename, bucket_name, filename)
	print('Image uploaded to S3 Bucket.')

# Rekognition Detect Text Function
def detectText():

	rekognitionClient = boto3.client('rekognition', aws_region)

	response = rekognitionClient.detect_text(
    		Image={
        		'S3Object': {
            		'Bucket': bucket_name,
            		'Name': filename
        	}
    	}
   	)

	print('The image contains the following text:')
        # Parse the JSON response from Amazon Rekognition, and print out detected lines of text.
	for text in response['TextDetections']:
		if (text['Type'] == 'LINE'):
			print ('Text: ' + text['DetectedText'] + ' was detected on line ' + str(text['Id']) + ' with confidence of ' + str(text['Confidence']))

# Campture Image Function
def captureImage():
    print('Capturing New Image...')
    camera.resolution = (1920, 1200)
    camera.vflip = True # orientation to capture photos to be modified based on how the camera is positioned
    camera.hflip = True # orientation to capture photos to be modified based on how the camera is positioned
    camera.capture(filename)
    print('New Image Captured.')

# Notice Function
def notice():
	print('*************************************************************')
	print('Disclaimer:')
	print('This Python script is only for demonstration purposes and')
	print('should NOT be used for any other purposes, or shared without')
	print('explicit permission from the author.')
	print('*************************************************************')

def main():
	notice() # Print disclaimer
	print('Started...')
	while True:
		print('--------------------------')
        	captureImage()
		# wait for the image to be camptured
        	time.sleep(2)
        	uploadImage()
		# wait for the image to be uploaded
		time.sleep(5)
		detectText()
		time.sleep(5)
	print('Done...')
main()
