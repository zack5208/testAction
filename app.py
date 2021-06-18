#!/usr/bin/env python3

import requests
import json
import os
import logging
import boto3
from botocore.exceptions import ClientError

##################################################
#var
##################################################
token = os.getenv('INPUT_TOKEN', None)
repo = os.getenv('INPUT_REPO', None)
default_repo = os.getenv('GITHUB_REPOSITORY', None)
ACCESS_KEY = os.getenv('INPUT_AWS_ACCESS_KEY_ID', None)
SECRET_KEY =  os.getenv('INPUT_AWS_SECRET_ACCESS_KEY', None)
SESSION_TOKEN = os.getenv('INPUT_AWS_SESSION_TOKEN', None)
s3_bucket = os.getenv('INPUT_S3_BUCKET', None)
version = os.getenv('INPUT_VERSION', None)



print(os.environ)
##################################################
#helper functions
##################################################
def download_url( url , save_path, chunk_size=128 ):
    r = requests.get( url, stream = True, headers={ 'Authorization' : 'token '+ token })
    with open( save_path , 'wb' ) as fd:
        for chunk in r.iter_content( chunk_size = chunk_size ):
            fd.write( chunk )

def upload_file(file_name, bucket,ACCESS_KEY ,SECRET_KEY,SESSION_TOKEN, object_name=None,):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=SESSION_TOKEN)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True            

##################################################
#Script start here
##################################################
#print("repo: " + repo)
print("default repo: " + default_repo)

if repo == "":
    repo = default_repo
print (type(repo))
print (repo == None)
print (repo)

url_get_release_latest_tag = "https://api.github.com/repos/" + repo + "/releases/latest"
url_download_release_latest = "https://github.com/" + repo + "/archive/"
print (url_get_release_latest_tag)
# Get the lastest version
if version == "":
    data = requests.get( url_get_release_latest_tag , headers = { 'Authorization' : 'token ' + token })
    dataObj = json.loads( data.content )
    latestTag = dataObj[ 'tag_name' ]
    version = latestTag
download_file_name = version + '.zip'
print (version)

# download the file to docker host
dst_download_file_path = os.getcwd()+ '/' + download_file_name
src_download_file_path = url_download_release_latest + '/' + download_file_name
download_url( src_download_file_path , dst_download_file_path )

# check file exists in the docker host
if os.path.exists(dst_download_file_path):
    print( "File exists: " + dst_download_file_path )
    print( "File size (bytes): " + str(os.path.getsize(dst_download_file_path)))
    # Upload zip file to S3
    if upload_file(dst_download_file_path,s3_bucket,ACCESS_KEY,SECRET_KEY,SESSION_TOKEN,download_file_name ):
        print ("Upload Successful!")
    else:
        print ("Upload fail!")    
else:
    print( "File dose not exist: " + dst_download_file_path )



