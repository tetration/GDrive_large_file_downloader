
#authors Tetration and nsadawi

#This is a modified version of nsadawi's Download-Large-File-From-Google-Drive-Using-Python
#nsadawi's original code repository https://github.com/nsadawi/Download-Large-File-From-Google-Drive-Using-Python
#I've adapted his code to accept Argument Parsers. This way all you need to do now when running his script 
#is to type it in your commandline the following way: Gdrive_downloader.py [GFileLink] [Destination]
#example: python .\Gdrive_downloader.py 3dasdp343343dswww43 C:\Git\test\mytext.txt 
#Voilà! You no longer need to modify this python script each time you want to download a different document or put it in a different destination
#All you have to do now is write the the ID and the final destination of each file you want to download from Google Drive
#Warning: All the files you want to dowload still need to be set to public in Google Drive otherwise this script wont be able to download them!

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("gfileID", help="your drive document ID right here")
parser.add_argument("gFileDestination", help="your gfile Destination")
args = parser.parse_args()

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

file_id = args.gfileID
destination = args.gFileDestination
download_file_from_google_drive(file_id, destination)
