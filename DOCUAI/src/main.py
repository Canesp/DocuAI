import os 

def add_api_key(api_key: str):
    os.environ["api_key"] = api_key

def main():
    print("Hello World!")