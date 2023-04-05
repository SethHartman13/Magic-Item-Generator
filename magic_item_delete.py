# Request libraries
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# Built in libraries
import json
import os
import time
import webbrowser

# Directory of destination folder
DB_FOLDER = "magic_items/common"

# Name of JSON to be deleted
FILE_NAME = "potion_of_healing.json"

# Index JSON
INDEX_JSON_DIR = f"{os.getcwd()}/storage_data/index.json"

# Unique DB ID
with open(INDEX_JSON_DIR, 'r') as f:
        index_json = json.load(f)

UNIQUE_ID = index_json[FILE_NAME]

# Database destination JSON
FULL_DB_URL = f"https://magic-items-a68a1-default-rtdb.firebaseio.com/{DB_FOLDER}/{UNIQUE_ID}.json"

# Authentication setup
SCOPES = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/firebase.database"
]
CREDENTIALS = service_account.Credentials.from_service_account_file(
    "credentials.json", scopes=SCOPES)

# -----------------------------------------------------------------------------------------------

# Authenticate session object
auth_session = AuthorizedSession(CREDENTIALS)

# Delete JSON from database
response = auth_session.delete(FULL_DB_URL)

# If the database says it was a good request
if response.status_code == 200:
    
    # Reads index JSON
    with open(INDEX_JSON_DIR, 'r') as f:
        index_json = json.load(f)

    # We remove the date from the index JSON dictionary
    del index_json[FILE_NAME]

    # Overwrites index JSON (with formatting)
    with open(INDEX_JSON_DIR, 'w') as f:
        json.dump(index_json, f, indent=4, sort_keys=True)
    
    print(f"{FILE_NAME} successfully deleted!")

# If the database says it was not a good request
else:
    print(f"Connection code error {response.status_code}")

    while True:
        user_input = input("Would you like to look up the status code? (Y/N) ")
        user_input.lower()

        if user_input == "y" or user_input == "yes" or user_input == "1":
            print("Your browser will pull up a wikipedia article.")
            time.wait(3)
            webbrowser.open(
                "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes")
            break
        elif user_input == "n" or user_input == "no" or user_input == "0":
            break

        else:
            print("Invalid input")