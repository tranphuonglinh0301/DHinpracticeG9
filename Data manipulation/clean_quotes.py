import csv

input_file = 'cleaned_dataset.csv'
output_file = 'processed_dataset.csv'

def clean_cell(cell):
    '''To remove unnecessary quotes from the end of each cell.'''
    if cell.endswith('""'):  
        return cell[:-2]  # Remove the last two characters
    return cell


with open(input_file, mode='r', encoding='utf-8') as infile, \
open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)  
    writer = csv.writer(outfile)  
        
    for row in reader:
        cleaned_row = [clean_cell(cell) for cell in row]
        writer.writerow(cleaned_row)