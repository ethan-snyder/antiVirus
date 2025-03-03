#from yara import *
import hashlib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")
api_hash = "3cf5901c94bc6788d5b274781f80184a8d94bb90eec261de0f43e75029624a0b" # SHA-256 hash of API KEY

# This function hashes the api key with sha-256 and checks it with the store api_hash variable above
def check_api_key(api_key, api_hash):
    hashed_key = hashlib.sha256(api_key.encode('utf-8')).hexdigest()

    if hashed_key == api_hash:
        print("API key is valid.")
        return True
    else:
        print("API key is invalid.")
        return False


# Checks if api_key exists, if it exists, it uses the check_api_key function for validity.
if api_key is None:
    print("API key not found in environment variables.")
else:
    check_api_key(api_key, api_hash) # Check the API key

# Simple function to get the hash of a file from its file path
def getHashFromFile(filePath):
    with open(filePath, 'rb') as file:
        file_data = file.read()
        sha256_hash = hashlib.sha256(file_data).hexdigest()
        print(sha256_hash)
    return sha256_hash

# Initializing a knownHashes set. Function will take in a text file and read it line by line and writing
# it directly to the knownHashes set.
knownHashes = set() # Using a set for O(1) Processing
def writeHashesToSet(hashesTxt):
    with open(hashesTxt, 'r') as file:
        for line in file:
            knownHashes.add(line.strip())

def compareCurrHash(knownHashes, sha256_hash):
    if sha256_hash in knownHashes:
        print("Known virus hash match.")
        print(hash)
        return True
    else:
        return False

def checkSingleFile(filePath):
    currHash = getHashFromFile(filePath)
    compareCurrHash(knownHashes, currHash)

# Mainly just checking functionality for now
writeHashesToSet('knownHashes/knownHashes1.txt')
print(knownHashes)
print("Enter a known virus hash.")
knownHashInput = input()
compareCurrHash(knownHashes, knownHashInput)