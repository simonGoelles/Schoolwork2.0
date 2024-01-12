# visualizer.py
import matplotlib.pyplot as plt


def visualize_data(data):
    timestamps = [entry['timestamp'] for entry in data]
    prices = [entry['price'] for entry in data]

    plt.plot(timestamps, prices, marker='o', linestyle='-', color='b')
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.title('Price vs Timestamp')
    plt.show()
