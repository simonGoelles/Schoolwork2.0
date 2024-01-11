# test_importer_visualizer.py
import unittest
from importer import import_data
from visualizer import visualize_data


class TestImporterVisualizer(unittest.TestCase):

    def setUp(self):
        # Create a sample
        self.test_file_path = 'test_data.csv'
        with open(self.test_file_path, 'w') as test_file:
            test_file.write("Lenzing,170447112,34.75,EUR,Vienna;\n")
            test_file.write("Andritz,170447131,59.41,USD,New York;\n")
            test_file.write("EVN,170447132,28.55,EUR,Vienna;\n")
            test_file.write("EVN,170447133,31.18,USD,New York;\n")

    def tearDown(self):
        # for deletion of sample
        import os
        os.remove(self.test_file_path)

    def test_importer(self):
        data = import_data(self.test_file_path)
        self.assertEqual(len(data), 4)
        self.assertEqual(data[0]['name'], 'Lenzing')
        self.assertEqual(data[1]['currency'], 'USD')

    def test_visualizer(self):
        data = import_data(self.test_file_path)
        self.assertIsNone(visualize_data(data))


if __name__ == '__main__':
    unittest.main()
