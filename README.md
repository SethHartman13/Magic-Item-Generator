# Overview

I wanted to further my understanding and development of cloud databases as I wanted to work more with REST APIs.

I have written 4 distinct programs that fullfill the following HTTP requests:
- delete (Deletes JSON from DB)
- get (Retrieves JSON from DB)
- post (Adds JSON to DB)
- put (Updates JSON in DB)

All the programs are reliant on having the proper authentication to access the database, that is where google.oath2 comes into play because using Google Authentication service, I am able to ensure that I am the only one (or those who I allow) is able to access the database.

## Post

Post requires the following information from the user in order to post to the database:
1. JSON containing magic_item data
2. file location containing magic_item data

The program does the rest as it sends a POST request to the database with the authentication and new JSON data


## Put

Post requires the following information from the user in order to post to the database:
1. JSON containing magic_item data
2. file location containing magic_item data

The program does the rest as it sends a PUT request to the database with the authentication and updated JSON data

## Get

Get requires the following information from the user in order to get information from the database:
1. Magic_item rarity type
2. Number of magic_items desired

The program does the rest as it sends a GET request to the database with the authentication and returns the magic items with necessary details.

## Delete

Get requires the following information from the user in order to delete information from the database:
1. JSON containing magic_item data
2. file location containing magic_item data

The program does the rest as it sends a DELETE request to the database with the authentication.


I wrote this software because I was in need of a random loot generator for DnD campaigns that I run.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](https://youtu.be/7GfF6jDMv6Y)

# Cloud Database

I am using Google Firebase's Realtime Database that uses REST APIs to perform Post, Put, Delete, and Get operations.

Realtime Database uses a JSON based data structure, allowing for the altering and creating of content in the database that primarily focuses on JSONs.

# Development Environment

Visual Studio Code is the source code editor used to write the Python programs and the JSON files.

Python

Google Authentication Libraries:
- google.auth.transport.requests
- google.oauth2

Built-in Python Libraries:
- json - JSON creation/loading library
- random - Random number generation
- time - time-related library
- webbrowser - Allows for the opening of http content (websites)


# Useful Websites

- [Firebase Docs](https://firebase.google.com/docs)


# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Larger database
- Allow for the separation of item types within each rarity category 
- Find a way to circumnavigate the Unique IDs of the Firestone DB
- Rewrite magic_item_post to be more flexible as to where it can pull the JSON

# Attribution

This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of
the Coast LLC and available at [https://dnd.wizards.com/resources/systems-reference-document](https://dnd.wizards.com/resources/systems-reference-document). The
SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at
[https://creativecommons.org/licenses/by/4.0/legalcode](https://creativecommons.org/licenses/by/4.0/legalcode).