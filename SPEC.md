# Specification for Project 3 Python Module

## Overview

Project 3 emphasizes skills in using Git for version control, creating and managing Python virtual environments, and handling different types of data.
The project involves fetching data from the web, processing it using appropriate Python collections, and writing the processed data to files.

## Deliverable Names

- GitHub Repository:  **datafun-03-analytics**
- Documentation:      README.md
- Script:             **yourname_analytics.py**

## Start a New Project

Follow this common workflow to start a new project.

1. In your browser, create a GitHub project repository with a default README.md. Name the repo as specified above.
2. Clone your new repository down to your machine into your Documents folder.
3. Open your new project repository folder in the Documents folder of your machine in VS Code (if you haven't already).
4. In VS Code, add a useful .gitignore file with a line for .vsode/ and .venv/ and whatever else doesn't need to be tracked in the repository.
5. In VS Code, edit your README.md to record your commands, process, and notes so far.
6. In VS Code, open a terminal - PowerShell if Windows, zsh or bash if Mac/Linux.
7. Use the terminal to git add your files and folders to source control, and git commit your changes with a useful message (e.g. "initial commit"), and git push the changes up to GitHub.
8. Verify your GitHub repository.

## Objective

Create a Python module that demonstrates skills in fetching data from the web, processing it using Python collections, and writing the processed data to different file formats.

## Requirements

Create and Manage Project Virtual Environment

This project uses the requests package, which is not included in the Python Standard Library - we must install it. 
To keep our project separate from all other Python projects,
we will create and manage a local project virtual environment.
We'll install our packages into the local project virtual environment.
For the recommended process with detailed steps and commands, see [PROJECT_VIRTUAL_ENV.md](PROJECT_VIRTUAL_ENV.md).

### 1. Opening Docstring

In your Python file, create a docstring with a brief introduction to your project.

### 3. Import Dependencies (At the Top, After the Opening Docstring)

Organize your project imports near the top of the file, following conventions.
For example, standard library imports first, then external library imports, then local module imports. 
Continue to practice importing your own modules and reuse your prior code when building your project folders.
Follow conventional package import organization and aliasing. 
Import each package just once near the top of the file. 

Important: Be sure you have INSTALLED any external packages (those not in the Python Standard Library) into your active project virtual environment first. 

Note: if we use "import pathlib" as below, we must use "pathlib.Path" when working with a Path. Many other projects use "from pathlib import Path". When using this approach, you omit the initial pathlib in pathlib.Path, and just use Path.


### 4. Define Functions for Data Acquisition

Use the requests library to fetch data from specified web APIs or online data sources.
This will include JSON, CSV, and plain text data.
After a successful fetch, call the appropriate write function to save the data to a file.

Python fetch functions code examples:

```python

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

```

### 5. Define Functions to Write Data

Write functions to save content to different file types (e.g., text, CSV, JSON).

Python write functions code examples:

```python

def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")


def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(response.content)
        print(f"Excel data saved to {file_path}")
```

### 6. Write Functions to Process Data and Generate Output

Write functions to read, process, and write results using appropriate Python collections (lists, sets, dictionaries, etc.). Demonstrate understanding of each collection data type's characteristics and usage.

Process the fetched data using appropriate Python collections and generate insightful analytics. The results of the processing should be formatted and written into text files.

Function 1. Process Text Data:
Process text with lists and sets to demonstrate proficiency in working with text files.
Analyze text data to generate statistics like word count, frequency of words, etc., and format these findings into a readable text file.

Function 2. Process CSV Data:
Process CSV files with tuples to demonstrate proficiency in working with tabular data.
Extract and analyze data from CSV files to produce meaningful statistics, summaries, or insights, and save the insights as text files.

Function 3. Process Excel Data:
Extract and analyze data from Excel files to produce meaningful statistics, summaries, or insights, and save the insights as text files.

Function 4. Process JSON Data:
Process JSON data with dictionaries to demonstrate proficiency in working with labeled data.
Parse the JSON data to extract relevant information and present it in a simplified, human-readable text format.

### 7. Implement Exception Handling

We know that reading and writing files - especially fetching items from the web is unreliable.
Even with perfect code, there are many things that can go wrong.
Use try/except/finally and implement exception handling to catch known possible errors and handle them gracefully in at least one of your functions.

Python function with exception handling code example:

```python

def fetch_txt_data(folder_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        # Will raise an HTTPError 
        # if the HTTP request returns an unsuccessful status code

        # Assuming the response content is text data
        file_path = pathlib.Path(folder_name) / 'data.txt'
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
```

### 8. Define Main Function

Implement a `main()` function to test the folder creation functions and demonstrate the use of imported modules.

Python main() function code example:

```python
def main():
    ''' Main function to demonstrate module capabilities. '''

    print(f"Name: {yourname_attr.my_name_string}")

    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'

    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    
    json_url = 'http://api.open-notify.org/astros.json'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')

    # Find some data you care about. What format is it? How will you ingest the data?
    # What do you want to extract and write? What export format will you use?
    # Process at least TWO unique data sets and describe your work clearly.
    # Use the README.md and your code to showcase your ability to work with data.

```

Copies of the data files have been added to this repo. 
Click on a data file to view it. 
To save the data, click "Raw" in the upper right - this will show just the raw file content in your browser. 
In Chrome, right-click and select "Save as ..." to get a local copy to compare. 
This won't work for Excel files - save the .xls file directly from GitHub. 

### Conditional Script Execution (At the end of the file)

Ensure the main function only executes when the script is run directly,
not when imported as a module by using standard boilerplate code.

```python
if __name__ == '__main__':
    main()
```

## Module Design

The code should be clear, well-organized, and demonstrate good practices.
Include comments and docstrings for clarity.
