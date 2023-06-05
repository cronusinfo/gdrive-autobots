import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

# Set up credentials
credentials_path = 'C:/Users/cronus/Desktop/grivepy/creds.json' #replace your own
credentials = Credentials.from_service_account_file(credentials_path)
drive_service = build('drive', 'v3', credentials=credentials)

# Define a function to upload a file
def upload_file(file_path, folder_id):
    file_name = os.path.basename(file_path)
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    print(f'File uploaded: {file_name} (ID: {file["id"]})')

# Specify the folder ID where you want to upload the files
folder_id = '1reYil3itb55X1JcEvIKeRyskEAholhiI' # replace your own

# Specify the folder path from which you want to upload the files
folder_path = r'F:\caferoo\202306__' #replace your own


# Retrieve file paths from the folder
file_paths = []
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_paths.append(os.path.join(folder_path, filename))

# Upload each file
for path in file_paths:
    upload_file(path, folder_id)
