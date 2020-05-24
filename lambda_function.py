"""
Creates an ECR repository ,if it doesn’t already exist, to store the container images once built
Uploads the train.py and Dockerfile to an S3 bucket
Creates a Codebuild project and uses the above files with a buildspec.yml to start the process to build a container push the image to ECR.
"""
def lambda_handler(event,context):
	"""
	triggering webhook by changing this file
	"""
    print("Body content: ")
    print(event)
    """
    trigger another webhook
    trigger another webook
    trigger another webhook
    trigger another webhook
    """