import boto3
import zipfile
import os
import tempfile

s3_client = boto3.resource('s3')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    with tempfile.TemporaryDirectory() as tempdir:
        download_path = os.path.join(tmpdir, os.path.basename(key))

        s3_client.download_file(bucket_name, key, download_path)

        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extract(tempdir)

        for file in os.listdir(tempdir):
            if file != os.path.basename(key):
                s3_client.upload_file(os.path.join(tempdir, file), bucket_name, file)