# import_file.py
import csv
from datetime import datetime


def import_data(file_path, output_file_path='processed_data.csv'):
    data = []

    with open(file_path, newline='') as csvfile:
        try:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                # Remove semicolons from the last element if present
                if row and row[-1].endswith(';'):
                    row[-1] = row[-1][:-1]
                if len(row) == 5:
                    name, timestamp, price, currency, location = row
                    timestamp = datetime.utcfromtimestamp(int(timestamp))
                    price = float(price)
                    data.append({
                        'name': name,
                        'timestamp': timestamp,
                        'price': price,
                        'currency': currency,
                        'location': location
                    })
        except csv.Error as e:
            print(f"Error reading CSV: {e}")

    # Write the data to the output CSV file
    write_to_csv(data, output_file_path)

    return data


def write_to_csv(data, output_file_path):
    with open(output_file_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'timestamp', 'price', 'currency', 'location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in data:
            writer.writerow(entry)
