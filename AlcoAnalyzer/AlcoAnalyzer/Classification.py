import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor, MLPClassifier
import DBHelper as dh
import json

df = pd.read_csv('Dataset/student_v1.csv')
dataset = df.drop(['school','address', 'sex', 'famsize', 'Mjob', 'Fjob', 'schoolsup', 'famsup','higher','goout', 'absences' ,
                   'Pstatus', 'Fedu', 'Medu', 'age', 'studytime', 'reason',
                   'guardian', 'traveltime', 'failures', 'paid', 'activities', 'nursery',
                   'internet', 'romantic', 'famrel', 'freetime', 'health', 'G1', 'G2', 'G3'], axis=1)

# print(dataset.head(2))
# print(dataset.Dalc.unique())
# print(dataset.Walc.unique())
# # df_dalc = dataset.groupby('Dalc')['Dalc'].nunique()
# # df_dalc = dataset.Dalc.nunique()
# # df_dalc = pd.value_counts(dataset.Dalc.unique())
# df_dalc = pd.Series(dataset.Dalc)
# count = df_dalc.value_counts()
#
# df_walc = pd.Series(dataset.Walc)
# coumt_wl = df_walc.value_counts()
#
# print(count)
# print(coumt_wl)

def getdalccount():
    df_dalc = pd.Series(dataset.Dalc)
    count = df_dalc.value_counts()

    count = count.astype(np.str)
    print(count)
    count_dict = dict(count)
    print(count_dict)
    return count_dict

def getwalccount():
    df_walc = pd.Series(dataset.Walc)
    count_wl = df_walc.value_counts()
    count_w1 = count_wl.astype(np.str)
    count_wl_dict = dict(count_w1)
    return count_wl_dict

