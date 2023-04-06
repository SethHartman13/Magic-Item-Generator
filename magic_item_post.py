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

# File directory of JSONs
FILE_FOLDER = f"{os.getcwd()}/{DB_FOLDER}/"

# Index JSON
INDEX_JSON_DIR = f"{os.getcwd()}/storage_data/index.json"

# Database destination JSON
FULL_DB_URL = f"https://magic-items-a68a1-default-rtdb.firebaseio.com/{DB_FOLDER}.json"

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

# Names of all the files in
file_names = os.listdir(FILE_FOLDER)

# Reads index JSON
with open(INDEX_JSON_DIR, 'r') as f:
    index_json = json.load(f)

# For every json we see
for file in file_names:

    # Verifies if the file already exists within the index.json
    if file not in index_json.keys():
        
        # Creates path for JSON
        name = FILE_FOLDER + file

        # Reads JSON
        with open(name, 'r') as f:
            json_file = f.read()

        # Sends JSON to database
        response = auth_session.post(FULL_DB_URL, data=json_file)

        # If the database says it was a good request
        if response.status_code == 200:

            # Puts response into a json
            response_detail = response.json()

            # We add the added json name to the index file with the unique ID assigned by the db
            index_json[str(file)] = response_detail['name']

            # Overwrites index JSON (with formatting)
            with open(INDEX_JSON_DIR, 'w') as f:
                json.dump(index_json, f, indent=4, sort_keys=True)
                
            print(f"{file} successfully added!")

        # If the databases says it was not a good request
        else:
            print(
                f"Response came back with status code {response.status_code} with {file}")

            while True:
                user_input = input(
                    f"Would you like to look up status code {response.status_code}? (Y/N) ")
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
                    
    # If the file already exists within index.JSON
    else:
        print(f"{file} already exists with unique ID {index_json[file]}")
