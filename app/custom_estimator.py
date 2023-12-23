from sklearn.ensemble import RandomForestClassifier
import numpy as np

class CustomEstimator:
    def __init__(self, false_ratio):
        self.false_ratio = false_ratio
        self.classifiers = []

    # Train the model using the ensemble approach introduced in the notebooks.
    def fit(self, X, y):
        num_true_records = sum(y == True) * self.false_ratio
        num_false_records = sum(y == False)
        
        num_classifiers = num_false_records // num_true_records
        false_records_index = y.index[y == False].tolist()
        true_records_index = y.index[y == True].tolist() 

        for i in range(num_classifiers):
            from_ = i * num_true_records
            to_ = (i * num_true_records) + num_true_records
            false_train_index = false_records_index[from_: to_]

            X_ = X.loc[false_train_index + true_records_index]
            y_ = y.loc[false_train_index + true_records_index]
            idx = np.random.permutation(X_.index)
            X_.reindex(idx)
            y_.reindex(idx)
            clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
            clf.fit(X_, y_)
            self.classifiers.append(clf)
            
    def fit_transform(self, X, y):
        self.fit(X, y)
        return self.predict(X)

    # Defining a prediction function based on the voting approach.
    def predict(self, X):
        f = lambda y: -1 if y == 0 else 1
        f_inv = lambda y: 0 if y < 0 else 1
        prediction = np.zeros(len(X))
        
        for clf in self.classifiers:
            y_hat = clf.predict(X).astype(int)
            prediction = prediction + np.array(list(map(f, y_hat)))
        
        return np.array(list(map(f_inv, prediction)))