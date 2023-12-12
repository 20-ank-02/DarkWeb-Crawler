import csv
import os

csv.field_size_limit(1000000000)

def remove_duplicates(input_file):
    # Keep track of seen rows
    seen_rows = set()
    print(f"./Output CSVs/{input_file}")
    # Open input and output files
    with open(f"./Output CSVs/{input_file}", 'r', newline='',encoding='utf-8') as file_in, open(f"./Output CSVs/clean/clean_{input_file}", 'w', newline='',encoding='utf-8') as file_out:
        
        reader = csv.reader(file_in)
        writer = csv.writer(file_out)

        # Iterate through each row in the input file
        for row in reader:
            # Convert row to tuple to use in set
            row[0]=str(row[0].replace('\n', ''))
            row[0]=str(row[0].replace('\r', ''))
            row[0]=str(row[0].replace('\t', ''))
            if row[0]=="":
                continue
            row_tuple = tuple(row)
            if row_tuple not in seen_rows:
                # If the row is unique, write it to the output file
                seen_rows.add(row_tuple)
                writer.writerow(row)


def merge_csv_files(input_folder, output_file):
    # Get a list of all CSV files in the input folder
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]

    # Initialize a flag to write header only once
    write_header = True

    # Open the output file in write mode
    with open(output_file, 'w', newline='',encoding="utf-8") as output_csv:
        csv_writer = csv.writer(output_csv)

        # Iterate through each CSV file
        for file_name in csv_files:
            file_path = os.path.join(input_folder, file_name)

            # Open each CSV file
            with open(file_path, 'r', newline='',encoding="utf-8") as input_csv:
                csv_reader = csv.reader(input_csv)

                # Skip the header if it's not the first file
                if not write_header:
                    next(csv_reader)

                # Write the rows to the output CSV file
                for row in csv_reader:
                    csv_writer.writerow(row)

                # Set the flag to False after writing the header
                write_header = False


def show_data(inputFileName):
    with open(inputFileName, 'r', newline='',encoding='utf-8') as file:
        reader=csv.reader(file)
        i=0
        for row in reader:
            if i==1526:
                print(row)
            i+=1
            

if __name__ == "__main__": 
    input_folder_path = './Output CSVs/'  

    csv_files = [file for file in os.listdir(input_folder_path) if file.endswith('.csv')]

    for csv_file in csv_files:
        remove_duplicates(csv_file)
    merge_csv_files("./Output CSVs/clean/","dataset.csv")
    show_data("dataset.csv")
        


