"""
Author: Joshua De los Santos
Modified: 1:24PM - 8/11/2018

Description:
    Methods to build, update and save a random forest classifier.
"""
import pandas as pd
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


RF_model_file = 'RF_model.joblib'
emotion_training_set = 'emotion_training_set.csv'


def update_Random_Forest():  # pragma: no cover
    """Build a random forest classifier for azure data
    :return: Random Forest Model
    """
    rfdf = pd.read_csv(emotion_training_set)
    target_column = rfdf['satisfaction']
    del rfdf['satisfaction']
    xTrain, xTest, yTrain, yTest = train_test_split(rfdf,
                                                    target_column,
                                                    test_size=0.5,
                                                    stratify=target_column,
                                                    random_state=736251)
    irs_rf = RandomForestClassifier(n_estimators=100,
                                    oob_score=True,
                                    random_state=487368)
    irs_rf.fit(xTrain, yTrain)
    accuracy_score(yTest, irs_rf.predict(xTest))
    return irs_rf


def build_New_Forest(partition, random_int, estimators, criteria, random):  # pragma: no cover
    """Build a random forest classifier for azure data
    :return: Random Forest Model
    """
    rfdf = pd.read_csv(emotion_training_set)
    target_column = rfdf['satisfaction']
    del rfdf['satisfaction']
    xTrain, xTest, yTrain, yTest = train_test_split(rfdf,
                                                    target_column,
                                                    test_size=partition,
                                                    stratify=target_column,
                                                    random_state=random_int)
    irs_rf = RandomForestClassifier(n_estimators=estimators,
                                    criterion=criteria,
                                    oob_score=True,
                                    random_state=random)
    irs_rf.fit(xTrain, yTrain)
    print("Validation Accuracy: ", accuracy_score(yTest, irs_rf.predict(xTest)))
    return irs_rf


def test_model_accuracy(model):
    return


def update_To_File(model):  # pragma: no cover
    """Saves model to a .joblib file
    :param model: sklearn classifier object
    """
    joblib.dump(model, RF_model_file)


def RF_To_File(model, file_path):
    joblib.dump(model, file_path)


def load_RF_File():
    """Load .joblib model file
    :return: classifier object
    """
    return joblib.load(RF_model_file)
