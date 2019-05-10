import os
import csv

class DataHandler():
    def __init__(self, csv_path=None, pickle_path=None):
        self._data_set = []
        self._data = []
        self._target =[]

        if csv_path != None:
            print(f'Loading CSV at \'{csv_path}\'')
            with open(csv_path, newline='') as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                for row in reader:
                    self._data_set.append(row)
        elif pickle_path != None:
            print(f'Loading Pickle at \'{pickle_path}\'')
            pickle_in = open(pickle_path, 'rb')
            self._data_set = pickle.load(pickle_in)

    @property
    def data_set(self):
        return self._data_set

    @property
    def data(self):
        return self._data

    @property
    def target(self):
        return self._target

    # generate the data set with labels
    def feat_set(self):
        for o in self._data_set:
            pass

    # dump data set for later
    def dump_data(self):
        pickle_out = open('data_set.pickle', 'wb')
        pickle.dump(self._data_set)

class DataHandlerException(Exception):
    def __init__(self, msg):
        self.msg = msg
