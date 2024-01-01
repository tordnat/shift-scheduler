import sys
import os
from excel_schedule_parser import *

def validate_arguments(args):
    """
    Validates the command line arguments.

    @param args List of command line arguments.
    @return Tuple containing the number of test data, the file path of the schedule, and the path to store test data.
    @exception SystemExit If any argument validation fails.
    """
    if len(args) != 4:
        print("Usage: generate_test_data.py <number_of_test_schedule_preferences> <file_path_of_schedule> <path_to_store_test_data>")
        sys.exit(1)

    try:
        num_test_data = int(args[1])
    except ValueError:
        print("The first argument must be an integer.")
        sys.exit(1)

    file_path = args[2]
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        sys.exit(1)

    directory_path = args[3]
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        sys.exit(1)

    return num_test_data, file_path, directory_path

def save_test_schedules(directory_path, file_name, test_schedule_array):
    """
    Saves each employee's shift preferences to an Excel file.

    @param directory_path The directory path where the Excel files will be saved.
    @param file_name The base name for the output files.
    @param test_schedule_array Array of DataFrames, each containing an employee's shift preferences.
    @exception Exception If an error occurs during file saving.
    """
    try:
        for i, schedule in enumerate(test_schedule_array):
            file_path = os.path.join(directory_path, f"{file_name}_{i}.xlsx")
            schedule.to_excel(file_path)
    except Exception as e:
        print(f"Error saving files: {e}")
        sys.exit(1)

def main():
    num_test_data, file_path, directory_path = validate_arguments(sys.argv)
    
    test_data_filename = os.path.splitext(os.path.basename(file_path))[0]
    schedule = open_schedule(file_path)
    test_schedule_array = generate_n_employee_shift_preferences(num_test_data, schedule, MIN_PREFERENCE, MAX_PREFERENCE)
    
    save_test_schedules(directory_path, test_data_filename, test_schedule_array)
    print(f"Stored {num_test_data} employee shift preferences to: {directory_path}")

if __name__ == "__main__":
    main()
