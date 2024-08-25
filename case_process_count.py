''' 
Perform data processing (counts) with Python
Author: Denise Case

This script demonstrates how to read and process various types of data 
(Excel, JSON, txt, csv). 

For now, our processing will just call the associated count function.
Different types of data involve different kinds of counts.  

- Excel (count rows)
- JSON (count records)
- Text (count lines)
- CSV (count rows)

We could create other processing functions. For example:

- force all text to capital letters
- find hyperlinks
- assess the sentiment
- perform analytics

'''

#####################################
# Import Modules
#####################################

# Standard library imports
import csv
import json
import pathlib 

# External library imports (requires virtual environment)
import openpyxl

# Local imports
# TODO: Change to import your prior modules        
import case_project_setup      
import case_utils 
import case_fetcher

#####################################
# Declare Global Variables
#####################################

# Name the folder where we can find our fetched data files
fetched_folder_name = "fetched"

# Name the folder where we will store our processed output files
output_folder_name = "fetched_counts"


#####################################
# Define Functions to Process EXCEL File
#####################################

def count_rows_in_excel(file_path: pathlib.Path) -> int:
    """Count the number of rows in the first sheet of an Excel file."""
    print(f"FUNCTION CALLED: count_rows_in_excel with file_path={file_path}")
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active  # Get the active sheet
        return sheet.max_row  # Return the number of rows
    except IOError as e:
        print(f"ERROR reading Excel data from {file_path}: {e}")
        return 0

def process_excel_file(fetched_folder_name: str, filename: str, output_folder_name: str, output_filename: str) -> None:
    """Process an Excel file to count rows and save the result to a text file."""
    print(f"FUNCTION CALLED: process_excel_file with fetched_folder_name={fetched_folder_name}, filename={filename}, output_folder_name={output_folder_name}, output_filename={output_filename}")
    file_path = pathlib.Path(fetched_folder_name).joinpath(filename)
    
    try:
        row_count = count_rows_in_excel(file_path)
        result_string = f"Row count: {row_count}\n"
        case_fetcher.write_txt_file(output_folder_name, output_filename, result_string)
    except IOError as e:
        print(f"ERROR processing Excel data: {e}")

#####################################
# Define Functions to Process JSON File
#####################################

def count_letters_in_json(file_path: pathlib.Path) -> int:
    """Count the number of letters in the JSON file content."""
    print(f"FUNCTION CALLED: count_letters_in_json() file_path={file_path}")
    try:
        with file_path.open('r') as file:
            json_content = file.read()
            # Count only alphabetic characters (letters)
            letter_count = sum(1 for char in json_content if char.isalpha())
            print(f"IN FUNCTION {letter_count=}")
            return letter_count
    except IOError as e:
        print(f"ERROR reading JSON data from {file_path}: {e}")
        return 0

def process_json_file(fetched_folder_name: str, filename: str, output_folder_name: str, output_filename: str) -> None:
    """Process a JSON file to count letters and save the result to a text file."""
    print(f"FUNCTION CALLED: process_json_file with fetched_folder_name={fetched_folder_name}, filename={filename}, output_folder_name={output_folder_name}, output_filename={output_filename}")
    file_path = pathlib.Path(fetched_folder_name).joinpath(filename)
    
    try:
        record_count:int = count_letters_in_json(file_path)
        result_string:str = f"Record count: {record_count}\n"
        case_fetcher.write_txt_file(output_folder_name, output_filename, result_string)
    except IOError as e:
        print(f"ERROR processing JSON data: {e}")

#####################################
# Define Functions to Process TEXT File
#####################################

def count_lines_in_text(file_path: pathlib.Path) -> int:
    """Count the number of lines in a text file."""
    print(f"FUNCTION CALLED: count_lines_in_text with file_path={file_path}")
    try:
        with file_path.open('r') as file:
            return sum(1 for _ in file)
    except IOError as e:
        print(f"ERROR reading text data from {file_path}: {e}")
        return 0

def process_txt_file(fetched_folder_name: str, filename: str, output_folder_name: str, output_filename: str) -> None:
    """Process a text file to count lines and save the result to a text file."""
    print(f"FUNCTION CALLED: process_txt_file with fetched_folder_name={fetched_folder_name}, filename={filename}, output_folder_name={output_folder_name}, output_filename={output_filename}")
    file_path = pathlib.Path(fetched_folder_name).joinpath(filename)
    
    try:
        line_count = count_lines_in_text(file_path)
        processed_data = f"Line count: {line_count}\n"
        case_fetcher.write_txt_file(output_folder_name, output_filename, processed_data)
    except IOError as e:
        print(f"ERROR processing text data: {e}")

#####################################
# Define Functions to Process CSV File
#####################################

def count_rows_in_csv(file_path: pathlib.Path) -> int:
    """Count the number of rows in a CSV file."""
    print(f"FUNCTION CALLED: count_rows_in_csv with file_path={file_path}")
    try:
        with file_path.open('r', newline='') as file:
            reader = csv.reader(file)
            return sum(1 for _ in reader)
    except IOError as e:
        print(f"ERROR reading CSV data from {file_path}: {e}")
        return 0

def process_csv_file(fetched_folder_name: str, filename: str, output_folder_name: str, output_filename: str) -> None:
    """Process a CSV file to count rows and save the result to a text file."""
    print(f"FUNCTION CALLED: process_csv_file with fetched_folder_name={fetched_folder_name}, filename={filename}, output_folder_name={output_folder_name}, output_filename={output_filename}")
    file_path = pathlib.Path(fetched_folder_name).joinpath(filename)
    
    try:
        row_count = count_rows_in_csv(file_path)
        processed_data = f"Row count: {row_count}\n"
        case_fetcher.write_txt_file(output_folder_name, output_filename, processed_data)
    except IOError as e:
        print(f"ERROR processing CSV data: {e}")



#####################################
# Define main() function for this module.
#####################################

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    # TODO: Change this to use your module function and uncomment
    print(f"Byline: {case_utils.get_byline()}")

    # Reuse  create_folders_from_list() from imported module to make a folder for output files
    # We set the name as a global variable so the whole module can use it. 
    # Make sure we provide a LIST when using our function - wrap the single string in brackets
    # TODO: Change this to use your module function and uncomment
    case_project_setup.create_folders_from_list([output_folder_name])

    # Process each file and write the output
    process_excel_file(fetched_folder_name, 'feedback.xlsx', output_folder_name, 'count_feedback.txt')
    process_json_file(fetched_folder_name, 'astros.json', output_folder_name, 'count_astros.txt')
    process_txt_file(fetched_folder_name, 'romeo.txt', output_folder_name, 'count_romeo.txt')
    process_csv_file(fetched_folder_name, '2020_happiness.csv', output_folder_name, 'count_2020_happiness.txt')

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