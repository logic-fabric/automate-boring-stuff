"""Script to remove header from all CSV files in the current directory.
"""


import csv
import os


def find_all_csv_files():
    csv_files = [
        filename for filename in os.listdir() if filename.endswith('.csv')
    ]
    return csv_files

def read_csv_content(csv_filename):
    with open(csv_filename) as csv_file:
        csv_has_header = csv.Sniffer().has_header(csv_file.read(1024))

        # repositioning reader on the first line:
        csv_file.seek(0)
        reader = csv.reader(csv_file)

        if csv_has_header:
            content = [row for row in reader if reader.line_num != 1]
        else:
            content = [row for row in reader]

        return content

def rewrite_csv_without_header(csv_filename, content):
    if content:
        with open(f'headless-{csv_filename}', 'w', newline='') as headless_csv:
            writer = csv.writer(headless_csv)

            for row in content:
                writer.writerow(row)


if __name__ == '__main__':
    csv_files = find_all_csv_files()

    for filename in csv_files:
        content = read_csv_content(filename)
        rewrite_csv_without_header(filename, content)
