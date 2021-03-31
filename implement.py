import boto3


s3_client = boto3.client('s3')
response = s3_client.create_bucket(Bucket='my-coursework-bucket97', CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


# Get the service resource / SQS queue 

sqs_client = boto3.client("sqs", region_name="us-west-2")

response = sqs_client.create_queue(QueueName="my-new-queue",Attributes={"DelaySeconds": "0", "VisibilityTimeout": "60"})




# Upload audio files to s2 bucket

s3_client = boto3.client('s3')
with open("Audio1.mp3", "rb") as f:
    s3_client.upload_fileobj(f, "my-coursework-bucket97", "Audio1.mp3")



# Upload audio files to s2 bucket

s3_client = boto3.client('s3')
with open("Audio1.mp3", "rb") as f:
    s3_client.upload_fileobj(f, "my-coursework-bucket97", "Audio1.mp3")

s3_client = boto3.client('s3')
with open("Audio2.mp3", "rb") as f:
    s3_client.upload_fileobj(f, "my-coursework-bucket97", "Audio2.mp3")


s3_client = boto3.client('s3')
with open("Audio3.mp3", "rb") as f:
    s3_client.upload_fileobj(f, "my-coursework-bucket97", "Audio3.mp3")


    s3_client = boto3.client('s3')
with open("Audio4.mp3", "rb") as f:
    s3_client.upload_fileobj(f, "my-coursework-bucket97", "Audio4.mp3")
