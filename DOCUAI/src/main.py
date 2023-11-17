import os
import keyring
import argparse
from rich.console import Console
from writer import Writer

def find_file(file_name: str) -> bool:
    """Check if a file exists in the current directory."""
    current_dir = os.getcwd()

    for file in os.listdir(current_dir):
        if file == file_name:
            return True
    
    return False


def add_api_key(args):
    """Function to set the API key."""
    console = Console()
    console.print(f"[bold]{'─' * 35} Setting API Key {'─' * 35}[/bold]")

    # Check if an API key is already set
    if keyring.get_password("DOCUAI", "api_key") is not None:
        console.print("[bold red]Warning:[/bold red] You already have an API key set. Do you want to overwrite it? (Y/n)\n")
        user_input = input("Input: ")

        if user_input.lower() != "y":
            console.print("[bold green]Success:[/bold green] API key not set.")
            return

    # Set the API key
    keyring.set_password("DOCUAI", "api_key", args.key)
    console.print("[bold green]Success:[/bold green] API key set.")


def document(args):
    """Function to generate documentation."""
    console = Console()

    # Check if an API key is set
    if keyring.get_password("DOCUAI", "api_key") is None:
        console.print("[bold red]Error:[/bold red] No API key set. Use 'docuai set_key' to set an API key.")
        return
    
    console.print(f"[bold]{'─' * 35} Generating documentation {'─' * 35}[/bold]")

    # Check if README.md file already exists
    if find_file("README.md"):
        console.print("[bold red]Warning:[/bold red] A README.md file already exists in this directory. Do you want to overwrite it? (Y/n)\n")
        user_input = input("Input: ")

        if user_input.lower() != "y":
            console.print("[bold green]Success:[/bold green] README.md file not generated.")
            return
    
    # Generate README.md file using Writer class
    writer = Writer()
    result = writer.write(notes=args.notes)

    if result:
        console.print("[bold green]Success:[/bold green] README.md file generated.")
    else:
        console.print("[bold red]Error:[/bold red] README.md file failed to be generated.")


def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="DOCUAI documentation generator")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Sub-parser for setting the API key
    parser_set_key = subparsers.add_parser("set_key", help="Add API key")
    parser_set_key.add_argument("key", help="API key")
    parser_set_key.set_defaults(func=add_api_key)

    # Sub-parser for generating documentation
    document_parser = subparsers.add_parser("document", help="Document project")
    document_parser.add_argument("notes", help="Notes")
    document_parser.set_defaults(func=document)

    args = parser.parse_args()

    # If no arguments are provided, print help message
    if not vars(args):
        parser.print_help()
    else:
        args.func(args)


if __name__ == '__main__':
    main()