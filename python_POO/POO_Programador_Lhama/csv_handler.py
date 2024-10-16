class CsvHandler:
    def __init__(self, directory):
        self.dir = directory

    def insert_data_in_csv(self, data):
        print(f'Inserindo {data} em {self.dir}')

    def read_data(self):
        print(f'read data in {self.dir}')

csv_handle = CsvHandler('12345678910')
csv_handle.read_data()