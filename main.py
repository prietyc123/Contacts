from __future__ import print_function
import httplib2
import os, io
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaIoBaseDownload

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import auth
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive Api Python'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.get_credential()

http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http= http)

def listFile(size):
    results = drive_service.files().list(
        pageSize=size, field="nextPageToken, file(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('files not found')
    else:
        print('Files:')

    for item in items:
        print('{0} ({1})'.format(item['name'], item['id']))

def downloadFile(file_id,filepath):

    req = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downld = MediaIoBaseDownload(fh, req)
    down = False
    while down is False:
        status, down = downld.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with io.open(filepath,'wb') as f:
        fh.seek(0)
        f.write(fh.read())

downloadFile('1-G52snk5YcwoG6RMVnE7z1pUbElvzM8o','Flower.jpeg')

