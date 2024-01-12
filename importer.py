import csv
from datetime import datetime


def import_data(file_path):
    data = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
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

    return data
