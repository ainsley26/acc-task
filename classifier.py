from data_handler import *
from sklearn.neighbors import KNeighborsClassifier

# Load data
names = DataHandler(csv_path='name_gender.csv')

# Slice data
names.slice_data(8)

# Create the classifier
knnc = KNeighborsClassifier(n_neighbors=5)
knnc.fit(names.trn_data, names.trn_target)

# Validate the classifier
trn_score = knnc.score(names.trn_data, names.trn_target)
tst_score = knnc.score(names.tst_data, names.tst_target)
print(f'CL: Classifier evaluation:\n       trn: {trn_score}\n       tst: {tst_score}')

def predict_name(name):
    f = names.data_to_feat(name)
    return knnc.predict([f])
