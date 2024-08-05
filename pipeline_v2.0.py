import pandas as pd
import os
import pathlib
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import Google

# Checking Current Dir. / other dir. stuff
cwd = os.getcwd()
os.chdir('/Users/databugh/Desktop/ev_data')
file_folder = os.listdir()
# Upload new data:
directory_output = '/Users/databuhg/Desktop/transformed_data'
os.makedirs(directory_output,exist_ok=True )

# Define needed functions here:
def program_price(program):
    if program in ['Puppy Preschool', 'Basic Obedience', 'Advanced Obedience']:
        return 135
    elif program in ['Day Training', 'Behavior Modification', 'Service Animal']:
        return 150
    elif program == '2 Dog Session':
        return 215
    else:
        return 0
# Extra:
file_num = 1
csv_files = []

# Parsing through the files in the folder and transforming the data
file_folder = os.listdir()
if file_folder:
    for files in file_folder:
        if files == 'pipeline.py':
            pass
        if files.endswith('.csv'):
            df = pd.read_csv(files)
            newdf = df[['Invitee Name', 'Invitee Email', 'Text Reminder Number', 'Event Type Name', 'Start Date & Time', 'End Date & Time', 'Canceled']]
            newdf.loc[:,'Start Date & Time'] = pd.to_datetime(newdf['Start Date & Time'], format='mixed')
            newdf.loc[:,'End Date & Time'] = pd.to_datetime(newdf['End Date & Time'], format='mixed')
            newdf.loc[:, 'Start Date & Time'] = newdf['Start Date & Time'].dt.strftime('%m-%d-%Y')
            newdf.loc[:, 'End Date & Time'] = newdf['End Date & Time'].dt.strftime('%m-%d-%Y')
            filterdf = newdf[newdf['Canceled'] == False ]
            filterdf.insert(7, "Price", pd.Series([], dtype='float'))
            filterdf.loc[:,'Price'] = filterdf['Event Type Name'].apply(program_price)
            evdatanew = filterdf
            print("Transforming Data")
            file_name = f'evdata{file_num}.csv'
            file_path = os.path.join(directory_output, file_name)
            csv_files.append(file_path)
            evdatanew.to_csv(file_path)
            file_num += 1
            print("Downloading new csv")

transformed_files = os.listdir(directory_output)


for tfile in transformed_files:
    ntfile = os.path.join(directory_output, tfile)
    # Authenticating 
    client_secrets_file = '/Users/databuhg/Desktop/google_secret.json'
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(client_secrets_file)
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    scopes=['https://www.googleapis.com/auth/drive']

    #Upload Folder To Drive:
    file1 = drive.CreateFile({'tittle' : 'practevdata'})
    print("Adding a tittle to your google sheet")
    file1.SetContentFile(ntfile)
    print("Setting up the csv to be uploaded")
    file1.Upload()
    print("Uploaded Successfully")
