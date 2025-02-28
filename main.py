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
    # Check the API key
    check_api_key(api_key, api_hash)