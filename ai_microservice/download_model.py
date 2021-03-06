import boto3
import botocore
import zipfile
import sys 

# this is just to demo. real use should use the config 
# environment variables or config file.
#
# See: http://boto3.readthedocs.org/en/latest/guide/configuration.html

session = boto3.session.Session(
    aws_access_key_id=sys.argv[1], 
    aws_secret_access_key=sys.argv[2]
)

s3 = session.resource("s3")
bucket = s3.Bucket(sys.argv[3])
KEY = sys.argv[4]
file = 'pipeline.zip'
try:
    bucket.download_file(KEY, file)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

zip_ref = zipfile.ZipFile('pipeline.zip', 'r')
zip_ref.extractall('.')
zip_ref.close()


