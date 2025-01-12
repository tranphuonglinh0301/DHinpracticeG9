import csv

input = 'processed_dataset.csv'
output = 'dataset_verified_users.csv'

filter = 'user_is_verified'

with open(input, mode='r', newline='', encoding='utf-8') as infile,\
open(output, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)  # Uses the first row as keys
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader() # Write the header row to the output file

    for row in reader:
        if row[filter] == 'true':
            writer.writerow(row)

