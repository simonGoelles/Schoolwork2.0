# visualiser.py
import matplotlib.pyplot as plt
import numpy as np


def visualize_data(data):
    unique_companies = set(entry['name'] for entry in data)
    company_colors = plt.cm.get_cmap('tab10', len(unique_companies))

    plt.figure(figsize=(10, 6))

    for i, company in enumerate(unique_companies):
        company_data = [entry for entry in data if entry['name'] == company]
        cities = set(entry['location'] for entry in company_data)
        city_colors = company_colors(i / len(unique_companies))

        for city in cities:
            city_data = [entry for entry in company_data if entry['location'] == city]
            timestamps = [entry['timestamp'] for entry in city_data]
            prices = [entry['price'] for entry in city_data]

            plt.plot(timestamps, prices, marker='o', linestyle='-', color=city_colors, label=f'{company}')

    plt.xlabel('Timestamp (seconds since epoch)')
    plt.ylabel('Price')
    plt.title('Price vs Timestamp')
    plt.legend()
    plt.show()
