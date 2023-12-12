import csv
import os

def remove_duplicates(input_file, output_file):
    # Keep track of seen rows
    seen_rows = set()

    # Open input and output files
    with open(input_file, 'r', newline='') as file_in, open(output_file, 'w', newline='') as file_out:
        reader = csv.reader(file_in)
        writer = csv.writer(file_out)

        # Iterate through each row in the input file
        for row in reader:
            # Convert row to tuple to use in set
            row_tuple = tuple(row)
            if row_tuple not in seen_rows:
                # If the row is unique, write it to the output file
                seen_rows.add(row_tuple)
                writer.writerow(row)


input_filename = 'output.csv'  # Replace with your input CSV file name
output_filename = 'dataset.csv'  # Replace with the desired output file name

# remove_duplicates(input_filename, output_filename)



def merge_csv_files(input_folder, output_file):
    # Get a list of all CSV files in the input folder
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]

    # Initialize a flag to write header only once
    write_header = True

    # Open the output file in write mode
    with open(output_file, 'w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)

        # Iterate through each CSV file
        for file_name in csv_files:
            file_path = os.path.join(input_folder, file_name)

            # Open each CSV file
            with open(file_path, 'r', newline='') as input_csv:
                csv_reader = csv.reader(input_csv)

                # Skip the header if it's not the first file
                if not write_header:
                    next(csv_reader)

                # Write the rows to the output CSV file
                for row in csv_reader:
                    csv_writer.writerow(row)

                # Set the flag to False after writing the header
                write_header = False

# Example usage:
input_folder_path = 'folder_with_csv_files'  # Replace with the folder containing CSV files
output_csv_path = 'merged_output.csv'  # Replace with the desired output file name

merge_csv_files(input_folder_path, output_csv_path)
