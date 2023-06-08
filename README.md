# gdrive-autobots
A tool written in python code used to automate the process of transferring a file from your local device going to gdrive

# Usage and installation
1. Clone the repository using `git clone https://github.com/cronusinfo/gdrive-autobots.git`.
# Install the required dependencies:
2. Install the required dependencies `pip install google-api-python-client google-auth`

# Setup your API & json
+ Obtain the credentials for your Google Drive API service account:
+ Go to the `https://console.cloud.google.com/`
+ Create a new project or select an existing project.
+ Enable the Google Drive API for the selected project.
+ Create a service account and download the JSON credentials file.
+ Place the credentials.json file in the same directory as your Python script. `Set up credentials
credentials = Credentials.from_service_account_file('credentials.json')
drive_service = build('drive', 'v3', credentials=credentials)`

# Guide for setting up your folder ID from local to gdrive
+ In Google Drive, each folder and file is assigned a unique identifier called the "ID". The folder ID is a string that represents the unique identifier for a specific folder in Google Drive.
+ To find the folder ID:
+ Go to Google Drive (https://drive.google.com) and sign in with your Google account.
+ Locate the folder you want to upload files into.
+ Right-click on the folder and select "Get link" from the context menu.
+ A dialog box will appear with the folder's sharing settings.
+ The link in the dialog box will contain the folder ID. It will be a part of the URL after the id= parameter.
+ For example, if the URL looks like: https://drive.google.com/drive/folders/ABC123XYZ456, then the folder ID is ABC123XYZ456
+ # Specify the folder ID where you want to upload the files
ex `folder_id = '1reYil3itb55X1JcEvIKeRyskEAholhiI'`
+ Specify the folder path from which you want to upload the files
ex `folder_path = r'F:\caferoo\202306__'`


3. run your script by calling out the script from your terminal `python3 gdrive.py`
note make sure you are on the right directory

📖 How it works





