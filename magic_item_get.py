# Request libraries
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# Built in libraries
import json
import os
import random
import webbrowser
import time

# Max ammunition gained (for ammo)
MAX_AMMO = 20

# Min ammunition gained (for ammo)

MIN_AMMO = 5

# Authentication setup
SCOPES = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/firebase.database"
]
CREDENTIALS = service_account.Credentials.from_service_account_file(
    "credentials.json", scopes=SCOPES)

# Authenticate session object
auth_session = AuthorizedSession(CREDENTIALS)

# List of acceptable rarities
ACCEPTABLE_RARITY = ["common", "uncommon"]

# Collect input on rarity
while True:
    user_input = input("What rarity would you like? ")

    user_input.lower()

    if user_input in ACCEPTABLE_RARITY:
        break
    else:
        print("Invalid Input")

# Collect number of magic items
while True:
    try:
        item_count = int(input("How many magic items do you want? "))
        print()

    except:
        print("Invalid Input")

    else:
        break

# Target JSON
FULL_DB_URL = f"https://magic-items-a68a1-default-rtdb.firebaseio.com/magic_items/{user_input}.json"

# Get call to database
response = auth_session.get(FULL_DB_URL)

# If the database says it was a good request
if response.status_code == 200:

    # Puts data into usable format
    response_json = response.json()
    magic_item_tuples = list(response_json.items())

    # Loops through and grabs information from dictionary
    for _ in range(item_count):

        # Pulls information out of a random tuple
        _, item_dict = magic_item_tuples[random.randint(
            0, len(magic_item_tuples) - 1)]

        # Puts information into variables for later use
        item_type = item_dict['type'].lower()
        item_name = item_dict['name']
        item_details = item_dict['details']

        # If the magic item is a potion
        if item_type == "potion":
            print(f"Name: {item_name}")
            print(f"Details : {item_details}\n")

        # If the magic item is a scroll
        elif item_type == "scroll":
            spells = item_dict['spells']
            random_spell = spells[random.randint(0, len(spells) - 1)]

            print(f"Name: {item_name}: {random_spell}")
            print(f"Details: {item_details}\n")

        # If the magic item is armor
        elif item_type == "armor":
            armors = item_dict['armor_types']

            # Picks random armor from valid list
            random_armor = armors[random.randint(0, len(armors) - 1)]

            print(f"Name: {item_name} ({random_armor})")
            print(f"Details: {item_details}\n")

        # If the magic item is a weapon
        elif item_type == "weapon":
            base_weapons = item_dict['base_weapons']

            # If it is ammunition
            if base_weapons == None:

                # Random number of ammo
                number_of_ammo = random.randint(MIN_AMMO, MAX_AMMO)

                base_weapon = f"({number_of_ammo}x)"

            # If it is not ammunition
            else:

                ### IMPORTANT NOTE ###
                # base_weapons must be stored in a list, regardless of the number of base_weapons
                base_weapon = f"({base_weapons[random.randint(0,len(base_weapons) - 1)]})"

            print(f"Name: {item_name} {base_weapons}")
            print(f"Details: {item_details}\n")

        # If the magic item is a wondrous item
        elif item_type == "wondrous item":
            attunement = item_dict['attunement']

            # If attunement is required
            if attunement:
                special_attunement_details = item_dict['attunement_type']

            # If attunement is not requiremd
            else:
                special_attunement_details = "No attunement"

            print(f"Name: {item_name}")
            print(f"Special Attunement Details: {special_attunement_details}")
            print(f"Details: {item_details}")

        # If the magic item is invalid or has not been programmed yet.
        else:
            print(
                f"We received an incorrect item type of {item_type} from item {item_name}")

# If the databases says it was not a good request
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
