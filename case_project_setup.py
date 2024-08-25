''' This module provides functions for creating a series of project folders. '''

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
import pathlib
import sys
import time

# Import local modules
# TODO: Change this to import your module and uncomment
# import case_utils 

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # Create folders for each year in the range
    # Loop through each year in the given range
    # The range function will generate numbers from start_year to end_year, inclusive
    for year in range(start_year, end_year + 1):
        
        # Convert the year into a string to use as the folder name
        folder_name = f"{year}"
        
        # Create the full path for the new folder by joining the data path with the folder name
        folder_path = data_path.joinpath(folder_name)
        
        # Create the folder on the filesystem
        # The parents=True argument ensures that any missing parent directories are created as well
        # The exist_ok=True argument prevents an error if the folder already exists
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Log a message indicating that the folder was successfully created
        print(f"Created folder: {folder_path}")


  
#####################################
# Define Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = True) -> None:
    '''
    Create folders from a list.
    
    Arguments:
    folder_list -- the list of folder names
    to_lowercase -- convert folder names to lowercase (default is False)
    remove_spaces -- remove spaces from folder names (default is False)
    '''
    # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}")

    # Verify input: Ensure the input is a list
    if isinstance(folder_list, str):
        print(f"ERROR: Expected a list but received a string ({folder_list}). Please provide a list of folder names.")
        sys.exit(1)

    # Verify input: Check if folder_list is empty
    if not folder_list:
        print("Error: The folder list is empty. No folders to create.")
        sys.exit(1)  # Exit the program with a non-zero status to indicate an error

    # Loop through each folder name in the list
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")
        
        # Create the full path for the new folder
        folder_path = project_path.joinpath(folder_name)
        
        # Create the folder (ignore if it already exists)
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Log the creation of the folder
        print(f"Created folder: {folder_path}")


  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create prefixed folders from a list of names.
    
    Arguments:
    folder_list -- the list of folder names
    prefix -- the prefix to add to each folder name
    '''
    # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")

    # Create prefixed folder names using list comprehension
    # Syntax reads like "return prefix + name for each name in folder_list"
    prefixed_folders = [prefix + name for name in folder_list]

    # Create the folders using the previously defined function
    create_folders_from_list(prefixed_folders)

  
#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int, folder_names: list = None) -> None:
    '''
    Create folders periodically with a delay.
    
    Arguments:
    duration_seconds -- The time to wait between creating folders.
    folder_names -- The list of folder names to create periodically (default is None, will create numbered folders).
    '''
    # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds} and folder_names={folder_names}")

    if folder_names is None:
        print(f"ERROR reading Excel data from {file_path}: {e}")

    for folder_name in folder_names:
        folder_path = project_path.joinpath(folder_name)
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")
        time.sleep(duration_seconds)

  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    # TODO: Change this to use your module function and uncomment
    # print(f"Byline: {case_utils.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while loop
    duration_secs: int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Call function 2 with additional options to lowercase and remove spaces
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

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