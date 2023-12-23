from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectKBest
from category_encoders import MEstimateEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
import numpy as np
from custom_estimator import CustomEstimator


class PLOTUPipeline:

    # We create a pipeline by instantiating an object from the class.
    def __init__(self, categorical_features, numerical_features,
                 one_hot_encode_columns , target_encode_columns,
                 k=30, false_ratio=2):

        self.categorical_features = categorical_features
        self.numerical_features = numerical_features
        self.one_hot_encode_columns = one_hot_encode_columns
        self.target_encode_columns = target_encode_columns

        self.categorical_processor = Pipeline(
            steps=[("imputation_most_frequent" ,SimpleImputer(strategy="most_frequent").set_output(transform="pandas")),
                   ("onehot_encoding" ,OneHotEncoder(cols=self.one_hot_encode_columns).set_output(transform="pandas")),
                   ("target_encoding",MEstimateEncoder(cols=self.target_encode_columns, m=2).set_output(transform="pandas")),
                   ]
        )

        self.numerical_processor = Pipeline(
            steps=[("imputation_mean",
                    SimpleImputer(missing_values=np.nan, strategy="mean").set_output(transform="pandas")),
                   ]
        )

        self.preprocessor=ColumnTransformer(
            [("categorical",self.categorical_processor, self.categorical_features),
             ("numerical",self.numerical_processor, self.numerical_features)]
        )

        self.pipe = Pipeline(
            [
                ("preprocessing", self.preprocessor),
                ("reduce_dim", SelectKBest(mutual_info_classif, k=k).set_output(transform="pandas")),
                ("estimator", CustomEstimator(false_ratio=false_ratio)),
            ]
        )

    def fit(self, X_train, y_train):
        self.pipe.fit(X_train, y_train)
