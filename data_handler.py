import os
import csv
import copy
from numpy import array
import numpy as np

class DataHandler():
    def __init__(self, csv_path=None, pickle_path=None):
        self._raw_data = []
        self._data = []
        self._target = []
        self._tst_data = []
        self._tst_target = []
        self._trn_data = []
        self._trn_target = []

        if csv_path != None:
            print(f'DH: Loading CSV at \'{csv_path}\'')
            with open(csv_path, newline='') as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                for row in reader:
                    self._raw_data.append(row)
                self._raw_data = array(self._raw_data)
                self.process_raw_data()

    @property
    def raw_data(self):
        return self._raw_data

    @property
    def data(self):
        return self._data

    @property
    def target(self):
        return self._target

    @property
    def tst_data(self):
        return self._tst_data

    @property
    def tst_target(self):
        return self._tst_target

    @property
    def trn_data(self):
        return self._trn_data

    @property
    def trn_target(self):
        return self._trn_target

    # process the raw data
    def process_raw_data(self):
        print(f'DH: Processing raw data')
        for o in self._raw_data:
            # generate feature set for object
            feat = self.data_to_feat(o[0])
            self._data.append(feat)

            # male = 0, female = 1
            gender = 0 if (o[1] == 'M') else 1
            self._target.append(gender)
            # self._target.append(o[1])
        self._data = array(self._data)
        self._target = array(self._target)

    # slice the data set -- hardcoded currently
    def slice_data(self, num):
        # create the test set
        self._tst_data = self._data[::num]
        self._tst_target = self._target[::num]
        assert len(self._tst_data) == len(self._tst_target)

        # create the training set
        self._trn_data = copy.deepcopy(self._data)
        self._trn_target = copy.deepcopy(self._target)
        self._trn_data = np.delete(self._trn_data, np.s_[::num], 0)
        self._trn_target = np.delete(self._trn_target, np.s_[::num], 0)
        assert len(self._trn_data) == len(self._trn_target)
        assert len(self._tst_data) + len(self._trn_data) == len(self._data)

        print(f'DH: Set sizes:\n       tst: {len(self.tst_data)}\n       trn: {len(self.trn_data)}')

    # used to generate the feature representation
    def data_to_feat(self, o):
        name = o.lower()
        feat = [(int.from_bytes(name[0].encode('ascii'), 'little') - 97)/25.0,
                (int.from_bytes(name[:2].encode('ascii'), 'little') - 24929)/6425.0,
                (int.from_bytes(name[:3].encode('ascii'), 'little') - 6381921)/8026746.0,
                (int.from_bytes(name[-3:].encode('ascii'), 'little') - 6381921)/8026746.0,
                (int.from_bytes(name[-2:].encode('ascii'), 'little') - 24929)/6425.0,
                (int.from_bytes(name[-1:].encode('ascii'), 'little') - 97)/25.0,
                len(name)/20]
        return feat
