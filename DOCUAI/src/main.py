import os
import keyring 

def add_api_key(api_key: str):
    keyring.set_password("DOCUAI", "api_key", api_key)

def main():
    print("Hello World!")
