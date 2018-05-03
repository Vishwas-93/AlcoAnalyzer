import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
import DBHelper as dh

df = pd.read_csv('Dataset/student_v1.csv')
dataset = df.drop(['school','address', 'famsize', 'Pstatus', 'Fedu', 'guardian', 'traveltime', 'failures', 'famsup', 'paid', 'activities', 'nursery',
                   'internet', 'romantic', 'famrel', 'freetime', 'health', 'G1', 'G2', 'G3'], axis=1)
# mother_jobs=list(dataset['Mjob'].unique())
#
# mother_jobs_values=dataset['Mjob'].values
# # print(mother_jobs_values)
# data_mother_edu_labelEncoder = LabelEncoder()
# data_mother_edu_labelEncoder.fit(mother_jobs_values)
# dataset['Mjob']= data_mother_edu_labelEncoder.transform(mother_jobs_values)
#
#
# enc = OneHotEncoder()
# enc.fit(np.reshape(dataset['Mjob'].values, (-1,1)))
# dataset['Mjob'] = enc.transform(np.reshape(dataset['Mjob'].values, (-1,1))).toarray()
#
# print(dataset[99,:])
# print(dataset.shape)
X = pd.get_dummies(dataset)
# print(X.head(5))
y = df['G1'].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=0)

# print(X_train.shape)
X_norm = StandardScaler()
X_train = X_norm.fit_transform(X_train)
# print(X_test.shape)
X_test = X_norm.transform(X_test)
# print(X_test[1])
# print(X_test)


# regressor = LinearRegression()
# regressor.fit(X_train, y_train)
# y_pred_basic=regressor.predict(X_test)
# print("Basic Linear Model")
# print(r2_score(y_test, y_pred_basic ))

# mlp = MLPRegressor(500,batch_size=32,solver='lbfgs', alpha=0.001, verbose=True, max_iter=1000, random_state=0)
# mlp.fit(X_train, y_train)
# pickle.dump(mlp, open(filename, 'wb'))

# print(mlp.score(X_train, y_train))
#
# y_pred = mlp.predict(X_test)
# y_pred = np.reshape([int(x) for x in y_pred], (-1, 1))
# print("Neural:")
# print(r2_score(y_test, np.reshape(y_pred, (-1, 1))))
# print("end")
filename = 'g1model.sav'
def predictGradeOne(X):
    g1model = pickle.load(open(filename, 'rb'))
    y_pred=g1model.predict(np.reshape(X, (1, -1)))[0]
    # print(y_pred)
    return y_pred
#
def dataframeprep(values):
    x_forPred = pd.get_dummies(values, columns=['sex', 'mjob', 'fjob', 'reason','schoolsup','higher'])
    # x_forPred = pd.get_dummies(values)
    print(x_forPred.shape)
    # X = X_norm.transform(x_forPred)
    # val = predictGradeOne(X)
    # print(val)
#
# val =[15, "M", 3, "health", "health", "course", 4, "Yes", 5, "Yes", 5, 5]
# dataframeprep(val)
#
# # val = np.array().reshape(1,-1)
# # x_forPred = pd.DataFrame(data=val,  columns=('age', 'sex', 'medu', 'mjob', 'fjob', 'reason', 'studytime', 'schoolsup', 'goout',
# #                                     'higher', 'dalc', 'walc'))
# # print(x_forPred)
# # print(pd.get_dummies(x_forPred, columns=['sex', 'mjob', 'fjob', 'reason','schoolsup','higher']))

# data =dh.getalldetails('aa_aa.com')
# data = data.drop(labels=['fname','lname','email','password','famsup','isLogged'], axis=1)
# dataframeprep(data)
