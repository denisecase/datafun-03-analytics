''' 
Data fetcher - uses external package requests.
Author: Denise Case

This script demonstrates how to fetch and write various types of data 
(Excel, JSON, txt, csv). 

Different types of data require different handling when using the requests library. 
Here's how you should handle the various types of responses:

Excel (response.content)
- Use response.content to get the raw binary data, which is ideal for non-text files like Excel files.
- Use modern files (*.xlsx not xls)

JSON (response.json())
- Use response.json() to directly parse the JSON content into a Python dictionary or list. This method automatically decodes the JSON data from the response.

Text (response.text)
- Use response.text to get the content of the response as a string. This is useful for plain text files or HTML files, where the content is human-readable.

CSV (response.text)
- Like text files, CSV files are also plain text, so you would use response.text to get the content of a CSV file as a string. You can then parse this string using Python’s csv module if needed.

'''

#####################################
# Import Modules
#####################################

# Standard library imports
import csv
import json
import pathlib 

# External library imports (requires virtual environment)
import requests  
# NOTE: if you see an error that "requests could not be resolved", 
# Click the lightbulb / Quick Fix / Select New Interpreter and choose (.venv)
# (.venv) should appear in lower left status bar of VS Code
# Make sure you've created / activated / installed requests into your .venv

# Local imports
# TODO: Change to import your prior modules        
import case_project_setup      
import case_utils 

#####################################
# Declare Global Variables
#####################################

# Name the folder where you will store your fetched data files
fetched_folder_name = "fetched"

#####################################
# Define Functions to Fetch Excel Data
#####################################

def fetch_excel_file(folder_name:str, filename:str, url:str) -> None:
    """Fetch Excel data from the given URL and write it to a file."""
    print(f"FUNCTION CALLED: fetch_excel_file with folder_name={folder_name}, filename={filename}, url={url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  
        write_excel_file(folder_name, filename, response.content)
        print(f"SUCCESS: Excel file fetched and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Excel data: {e}")

def write_excel_file(folder_name:str, filename:str, binary_data:bytes) -> None:
    """Write Excel binary_data to a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: write_excel_file with file_path={file_path}")
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:
            file.write(binary_data)
        print(f"SUCCESS: Excel data saved to {file_path}")
    except IOError as e:
        print(f"Error writing Excel data to {file_path}: {e}")

#####################################
# Define Functions to Fetch JSON Data 
#####################################

def fetch_json_file(folder_name:str, filename:str, url:str) -> None:
    """Fetch JSON data from the given URL and write it to a file."""
    print(f"FUNCTION CALLED: fetch_json_file with folder_name={folder_name}, filename={filename}, url={url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  
        write_json_file(folder_name, filename, response.json())
        print(f"SUCCESS: JSON file fetched and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching JSON data: {e}")

def write_json_file(folder_name:str, filename:str, json_data) -> None:
    """Write JSON data to a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: write_json_file with file_path={file_path}")
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            json.dump(json_data, file, indent=4)
        print(f"SUCCESS: JSON data saved to {file_path}")
    except IOError as e:
        print(f"Error writing JSON data to {file_path}: {e}")

#####################################
# Define Functions to Fetch Text Data
#####################################

def fetch_txt_file(folder_name:str, filename:str, url:str) -> None:
    """Fetch text data from the given URL and write it to a file."""
    print(f"FUNCTION CALLED: fetch_txt_file with folder_name={folder_name}, filename={filename}, url={url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
        print(f"SUCCESS: Text file fetched and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching text data: {e}")

def write_txt_file(folder_name:str, filename:str, string_data:str) -> None:
    """Write text data to a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: write_txt_file() folder_name={folder_name}, filename={filename}, string_data={string_data}")

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        print(f"SUCCESS: Text data saved to {file_path}")
    except IOError as e:
        print(f"Error writing text data to {file_path}: {e}")

#####################################
# Define Functions to Fetch CSV Data
#####################################

def fetch_csv_file(folder_name:str, filename:str, url:str) -> None:
    """Fetch CSV data from the given URL and write it to a file."""
    print(f"FUNCTION CALLED: fetch_csv_file with folder_name={folder_name}, filename={filename}, url={url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
        print(f"SUCCESS: CSV file fetched and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching CSV data: {e}")

def write_txt_file(folder_name:str, filename:str, string_data:str) -> None:
    """Write text data to a file."""
    file_path = pathlib.Path(folder_name).joinpath(filename)
    print(f"FUNCTION CALLED: write_txt_file() folder_name={folder_name}, filename={filename}, string_data={string_data}")

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        print(f"SUCCESS: Text data saved to {file_path}")
    except IOError as e:
        print(f"Error writing text data to {file_path}: {e}")

#####################################
# Define main() function for this module.
#####################################

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Reuse get_byline() from imported module
    # TODO: Change this to use your module function and uncomment
    print(f"Byline: {case_utils.get_byline()}")

    # Reuse  create_folders_from_list() from imported module to make a folder for fetched files
    # We set the name as a global variable so the whole module can use it. 
    # Make sure we provide a LIST when using our function
    # TODO: Change this to use your module function and uncomment
    case_project_setup.create_folders_from_list([fetched_folder_name])

    # Web locations of different types of data to fetch
    # TODO: Optional find different urls for 4 different types of data                               
    excel_url:str = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/Feedback.xlsx' 
    json_url:str = 'http://api.open-notify.org/astros.json'
    txt_url:str = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/romeo.txt'
    csv_url:str = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    # Fetch data files - provide the fetched file names
    fetch_excel_file(fetched_folder_name, "feedback.xlsx", excel_url)
    fetch_json_file(fetched_folder_name, "astros.json", json_url)
    fetch_txt_file(fetched_folder_name, "romeo.txt", txt_url)
    fetch_csv_file(fetched_folder_name, "2020_happiness.csv", csv_url)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.
