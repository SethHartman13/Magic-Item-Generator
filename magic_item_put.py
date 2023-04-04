from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# Built in libraries
import json
import os

# Directory of file
DB_FOLDER = "magic_items/common/"

FILE_NAME = "spell_scroll_first.json"

# File location of JSON
FILE = f"{os.getcwd()}/{DB_FOLDER}/{FILE_NAME}"

# Index JSON
INDEX_JSON_DIR = f"{os.getcwd()}/storage_data/index.json"

# Authentication setup
SCOPES = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]
CREDENTIALS =  service_account.Credentials.from_service_account_file("credentials.json", scopes=SCOPES)

auth_session = AuthorizedSession(CREDENTIALS)


# Grab unique ID from the index JSON

with open(INDEX_JSON_DIR, 'r') as f:
  index_json = json.load(f)
  
unique_id = index_json[FILE_NAME]

full_db_url = f"https://magic-items-a68a1-default-rtdb.firebaseio.com/{DB_FOLDER}/{unique_id}.json"

# Reads changed JSON
with open(FILE, "r") as f:
  json_file = f.read()

# Sends JSON to database
response = auth_session.put(full_db_url, data=json_file)

# If the database says it was a good request
if response.status_code == 200:
  print("Success!")
  
# If the database says it was not a good request
else:
  print("Failure!")