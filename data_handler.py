import os

class DataHandler():
    'Generate data set'

    def __init__(self, csv_path=None, pickle_path=None):
        if csv_path == None and pickle_path == None:
            if not os.path.isfile('data_set.pickle')
                raise DataHandlerException(f'Data set is missing')
            else:
                pickle_in = open('data_set.pickle', 'rb')
                self._data_set = pickle.load(pickle_in)
        elif csv_path != None:
            print(f'Loading CSV at {csv_path}')
        elif pickle_path != None:
            print(f'Loading Pickle at {pickle_path}'
            pickle_in = open(pickle_path, 'rb')
            self._data_set = pickle.load(pickle_in)

class DataHandlerException(exception):
    def __init__(self, msg):
        self.msg = msg
