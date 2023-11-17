import os
import keyring 
import argparse
from rich.console import Console

from writer import Writer

def add_api_key(args):
    keyring.set_password("DOCUAI", "api_key", args.api_key)

def document(args):
    writer = Writer()
    writer.write()

def main():
    
    parser = argparse.ArgumentParser(description="DOCUAI documentation generator")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    add_api_key_parser = subparsers.add_parser("add_api_key", help="Add API key")
    add_api_key_parser.add_argument("api_key", help="API key")
    add_api_key_parser.set_defaults(func=add_api_key)

    document_parser = subparsers.add_parser("document", help="Document project")
    document_parser.add_argument("notes", help="Notes")
    document_parser.set_defaults(func=document)

if __name__ == '__main__':
    main()
