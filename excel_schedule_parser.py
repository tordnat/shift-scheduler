import os.path
import pandas as pd
import numpy as np
from bidict import bidict
from random_integer_generator import generate_random_integer_array

# Constants (Will be moved to config file eventually)
FILENAME = "schedule.xlsx"
MAX_PREFERENCE = 3
MIN_PREFERENCE = 0
INDEX_COLUMN = 0

# Mapping og number to preference
NUMBER_TO_PREFERENCE = bidict({0: "", 1: "X", 2: "XX", 3:"XXX"})

def map_number_to_pref(number : int):
    """
    @brief Maps a numeric preference to a string representation

    @arg number Numeric (integer) preference value
    @returns string String representation of preference value
    """
    return NUMBER_TO_PREFERENCE[number]

# Vectorize the mapping function for efficiency
vectorized_map_number_to_pref = np.vectorize(map_number_to_pref)


def open_schedule(file_path):
    """
    @brief Opens and reads an Excel schedule file.

    @arg file_path(str) Path to Excel file.
    @returns DataFrame Pandas DataFrame containing the schedule, or None if an error occurs. 
    """
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return None
    try:
        return pd.read_excel(file_path, sheet_name = 0, index_col=INDEX_COLUMN)
    except Exception as error:
        print(f"Error reading {file_path}: {error}")
        return None

def generate_n_employee_shift_preferences(num_employees, schedule, min_preference, max_preference):
    """
    @brief Generates random shift preference for a given number of employees.

    @arg num_employees(int) Number of employees.
    @arg schedule(DataFrame) DataFrame representing the schedule
    @arg min_preference(int) Minimum preference value
    @arg max_preference(int) Maximum preference value

    @returns List[DataFrame] List of DataFrames, each representing an empoyee's shift preference. 
    """
    return [generate_random_employee_shift_preference(schedule, min_preference, max_preference) for _ in range(num_employees)]
    
def generate_random_employee_shift_preference(schedule, min_preference, max_preference):
    """
    @brief Generates random shift preferences for a single employee based on a given schedule.

    @arg schedule(DataFrame) DataFrame representing the schedule.
    @arg min_preference(int) Minimum preference value.
    @arg max_preference(int) Maximum preference value.

    @return DataFrame DataFrame representing the employee's shift preferences.
    """
    schedule_copy = schedule.fillna("") # Fill empty cells with empty strings
    num_rows, num_columns = schedule_copy.shape
    num_shifts  = num_columns * num_rows
    # Generate random shift preferences
    random_shift_preferences = generate_random_integer_array(number=num_shifts, min_val=min_preference, max_val=max_preference)
    mapped_preferences       = vectorized_map_number_to_pref(random_shift_preferences)

    # Reshape to match the schedule shape (aka. 2 dim matrix)
    schedule_copy.iloc[:, :] = mapped_preferences.reshape(num_rows, num_columns)
    return schedule_copy

