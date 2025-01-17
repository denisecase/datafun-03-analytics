"""
Process a JSON file to count astronauts by spacecraft and save the result.

JSON file is in the format where people is a list of dictionaries with keys "craft" and "name".

{
    "people": [
        {
            "craft": "ISS",
            "name": "Oleg Kononenko"
        },
        {
            "craft": "ISS",
            "name": "Nikolai Chub"
        }
    ],
    "number": 2,
    "message": "success"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "example_data"
processed_folder_name: str = "example_processed"

#####################################
# Define Functions
#####################################

def count_astronauts_by_craft(file_path: pathlib.Path) -> dict:
    """Count the number of astronauts on each spacecraft from a JSON file."""
    try:
        with file_path.open('r') as file:
            # Use the json module load() function 
            # to read data file into a Python dictionary
            astronaut_dictionary = json.load(file)  
            # initialize an empty dictionary to store the counts
            craft_counts_dictionary = {}
            # people is a list of dictionaries in the JSON file
            people_list: list = astronaut_dictionary.get("people", [])
            for person_dictionary in people_list:  
                craft = person_dictionary.get("craft", "Unknown")
                craft_counts_dictionary[craft] = craft_counts_dictionary.get(craft, 0) + 1
            return craft_counts_dictionary
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""
    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, "astros.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, "json_astronauts_by_craft.txt")
    
    craft_counts = count_astronauts_by_craft(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Astronauts by spacecraft:\n")
        for craft, count in craft_counts.items():
            file.write(f"{craft}: {count}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")
