# DocuAI

## Overview
DocuAI is a powerful tool designed to automate the creation of documentation for projects. It leverages OpenAI's GPT models to generate comprehensive and concise README files based on the code and notes provided.

## Installation
To install DocuAI, you need to have git and pip already installed on your machine. Follow these steps to get started:

```
pip install git+https://github.com//Canesp/DocuAI.git#egg=DocuAI
```

## Commands and Setup

### Setting API Key
Before using DocuAI, you need to save your API key using the `set_key` command:

```
docuai set_key YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual OpenAI API key.

### Generating Documentation
To generate documentation for your project, use the `document` command with the notes you wish to include:

```
docuai document "Your project notes here."
```

This will trigger the process that analyzes your project files and notes to generate a `README.md` file.

## Files and Scripts Information
The DocuAI package contains several Python scripts:

- `setup.py`: Script that prepares the package for installation.
- `Writer`: A class responsible for writing notes into a `README.md` file using OpenAI. It handles API key retrieval, file management, and interactions with the OpenAI client.
- `main`: Contains the command-line interface for the package, allowing users to set API keys and initiate documentation generation.

## Footnote
This documentation was created using the DocuAI package. :sparkles:

---