import os
import keyring 
import argparse
from rich.console import Console

from writer import Writer

def find_file(file_name: str) -> bool:

    current_dir = os.getcwd()

    for file in os.listdir(current_dir):
        if file == file_name:
            return True
    
    return False

def add_api_key(args):

    console = Console()
    console.print(f"[bold]{'─' * 35} Setting API Key {'─' * 35}[/bold]")

    if keyring.get_password("DOCUAI", "api_key") is not None:
        
        console.print("[bold red]Warning:[/bold red] You already have an API key set. Do you want to overwrite it? (Y/n)\n")
        user_input = input("Input: ")

        if user_input.lower() == "y":
            console.print("[bold green]Success:[/bold green] API key set.")
        else:
            console.print("[bold green]Success:[/bold green] API key not set.")
            return
        
    keyring.set_password("DOCUAI", "api_key", args.key)
    console.print("[bold green]Success:[/bold green] API key set.")

def document(args):

    console = Console()

    if keyring.get_password("DOCUAI", "api_key") is None:
        console.print("[bold red]Error:[/bold red] No API key set. Use 'docuai set_key' to set an API key.")
        return
    
    console.print(f"[bold]{'─' * 35} Generating documentation {'─' * 35}[/bold]")

    if find_file("README.md"):
        console.print("[bold red]Warning:[/bold red] A README.md file already exists in this directory. Do you want to overwrite it? (Y/n)\n")
        user_input = input("Input: ")

        if user_input.lower() != "y":
            console.print("[bold green]Success:[/bold green] README.md file not generated.")
            return
    
    writer = Writer()
    result = writer.write(notes=args.notes)

    if result:
        console.print("[bold green]Success:[/bold green] README.md file generated.")
    else:
        console.print("[bold red]Error:[/bold red] README.md file failed to be generated.")

def main():
    
    parser = argparse.ArgumentParser(description="DOCUAI documentation generator")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    parser_set_key = subparsers.add_parser("set_key", help="Add API key")
    parser_set_key.add_argument("key", help="API key")
    parser_set_key.set_defaults(func=add_api_key)

    document_parser = subparsers.add_parser("document", help="Document project")
    document_parser.add_argument("notes", help="Notes")
    document_parser.set_defaults(func=document)

if __name__ == '__main__':
    main()
