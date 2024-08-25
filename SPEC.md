# Specification for Project 3 Python Module

## Overview

Project 3 emphasizes skills in using Git for version control, creating and managing Python virtual environments, and handling different types of data.
The project involves fetching data from the web, processing it using appropriate Python collections, and writing the processed data to files.

## Deliverable Names

Create a new GitHub repository with a default README.md. In your GitHub repository, create new empty Python script as named below. Add your earlier scripts to your project repo.

- GitHub Repository:  **datafun-03-analytics**
- Documentation:      README.md
- New Script:         **yourname_fetcher.py**
- Setup Script:       **yourname_project_setup.py**
- Utils Script:       **yourname_utils.py**

## Objective

Create a Python module that demonstrates skills in fetching data from the web, processing it using Python collections, and writing the processed data to different file formats.

## Requirements

### 1. Opening Docstring

In your Python file, create a docstring with a brief introduction to your project.

### 2. Import Dependencies (At the Top, After the Opening Docstring)

Organize your project imports near the top of the file, following conventions.
For example, standard library imports first, then external library imports (we don't need any of these yet), then local module imports. 
Follow conventional package import organization. 
Import each package just once near the top of the file.  

Important: Be sure you have INSTALLED any external packages (those not in the Python Standard Library) into your active project virtual environment first. 

Note: if we use "import pathlib", we must use "pathlib.Path" when working with a Path. 
Many other projects use "from pathlib import Path". 
When using this approach, you omit the initial pathlib in pathlib.Path, and just use Path.

### 3. Define Global Variables

Assign a global variable for the folder where you will store your fetched data files.

### 4. Define Functions for Data Acquisition

Use the requests library to fetch data from specified web APIs or online data sources.
This should include Excel, JSON, text, and CSV files. 
After a successful fetch, call the appropriate write function to save the data to a file.

For each type of source file:

- Write a function to fetch it using the requests module
- Write a function to write the data. This will be called by the fetch function and will be available for reuse as needed. 


### 5. Write Functions to Process Data and Generate Output

A file has been provided that will process each kind of data. 

In each case, it reads the fetched file and calls a function to process that file. 

Right now, all the files are processed using a count of some kind and the results are provided in the 'fetched_counts' output folder. 

You are encouraged to provide an additional process function as you like, but it is not required. 

### 6. Implement Exception Handling in Functions

Fetching items from the web is unreliable.
Even with perfect code, many things can go wrong.
When we know in advance our code might not work (due to no fault of our own) 
we plan for these expected errors. 
We use try/except/finally and implement exception handling to catch known possible errors and handle them gracefully in our functions.

Error handling is not often taught as it takes up twice the space, but all production code includes robust error handling. 

It is good professional practice to:

- LOG each function call (with the arguments)
- LOG errors
- LOG successful function returns (including any calculated outputs)

We use print() statements, but the standard library has a great logging module that improves on this important practice. 

### 7. Define Main Function

Implement a main() function to test the folder creation functions and demonstrate the use of imported modules.

Use this main() method or something similar to test your function implementations.

```python
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
```

### Conditional Script Execution (At the end of the file)

Ensure the main function only executes when the script is run directly,
not when imported as a module by using standard boilerplate code.

```python
if __name__ == '__main__':
    main()
```
