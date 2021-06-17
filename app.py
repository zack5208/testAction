#!/usr/bin/env python3

import requests
#from requests.auth import HTTPBasicAuth
import json
import os
#import sys

##################################################
#var
##################################################
token = os.getenv('INPUT_TOKEN', None)
owner = os.getenv('INPUT_OWNER', None)
repo = os.getenv('INPUT_REPO', None)

print(os.environ)
print( "owner : "+ owner)
print( "repo : "+ repo)
url_get_release_latest_tag = "https://api.github.com/repos/" + owner + "/"+ repo + "/releases/latest"
url_download_release_latest = "https://github.com/" + owner + "/"+ repo + "/archive/"

##################################################
#helper functions
##################################################
def download_url( url , save_path, chunk_size=128 ):
    r = requests.get( url, stream = True, headers={ 'Authorization' : 'token '+ token })
    with open( save_path , 'wb' ) as fd:
        for chunk in r.iter_content( chunk_size = chunk_size ):
            fd.write( chunk )

##################################################
#Script start here
##################################################
print(url_get_release_latest_tag)
print(url_download_release_latest)
data = requests.get( url_get_release_latest_tag , headers = { 'Authorization' : 'token ' + token })
dataObj = json.loads( data.content )
print(dataObj)
latestTag = dataObj[ 'tag_name' ]
download_file_name = latestTag + '.zip'
dst_download_file_path = os.getcwd()+ '/' + download_file_name
src_download_file_path = url_download_release_latest + '/' + download_file_name
download_url( src_download_file_path , dst_download_file_path )
# check file exists
if os.path.exists(dst_download_file_path):
    print( "File exists: " + dst_download_file_path )
    print( "File size (bytes): " + os.path.getsize(dst_download_file_path))
else:
    print( "File dose not exist: " + dst_download_file_path )