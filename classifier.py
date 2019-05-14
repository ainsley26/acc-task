from data_handler import *
from sklearn.neighbors import KNeighborsClassifier

class Classifier():
    def __init__(self, file_name, slice=8):
        # load data
        self.names = DataHandler(csv_path=file_name)
        self.names.slice_data(slice)

        # create classifier
        print(f'CL: Creating classifier and fitting')
        self.clf = KNeighborsClassifier(n_neighbors=3)
        self.clf.fit(self.names.trn_data, self.names.trn_target)

        # validate classifier
        print(f'CL: Validating classifier')
        self.trn_score = self.clf.score(self.names.trn_data, self.names.trn_target)
        self.tst_score = self.clf.score(self.names.tst_data, self.names.tst_target)
        print(f'CL: Classifier evaluation:\n       trn: {self.trn_score}\n       tst: {self.tst_score}')

    def predict_name(self, name):
        f = self.names.data_to_feat(name)
        return self.clf.predict([f])
