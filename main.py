# main.py
from importer import import_data
from visualizer import visualize_data


def main():
    file_path = 'testfile.csv'

    data = import_data(file_path, output_file_path='processed_data.csv')

    visualize_data(data)


if __name__ == "__main__":
    main()
