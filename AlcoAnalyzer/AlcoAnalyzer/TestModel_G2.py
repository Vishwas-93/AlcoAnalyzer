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
dataset = df.drop(['school','address', 'famsize', 'Pstatus', 'Fedu', 'guardian', 'traveltime', 'failures', 'paid', 'activities', 'nursery',
                   'internet', 'romantic', 'famrel', 'freetime', 'health', 'G1', 'G2', 'G3'], axis=1)
# y = df['G1'].values


g1 = df['G1'].values
y = df['G2'].values

# print(dataset.head(2))
 # 'mjob','sex', 'fjob', 'reason','schoolsup','higher'
'''Mother JOB'''
mother_jobs_values=dataset['Mjob'].values
data_mother_job_labelEncoder = LabelEncoder()
data_mother_job_labelOneHot =OneHotEncoder()
mother_jobs_values=data_mother_job_labelEncoder.fit_transform(mother_jobs_values)
mother_jobs_values =data_mother_job_labelOneHot.fit_transform(np.reshape(mother_jobs_values,(-1,1)))
mother_jobs_values=mother_jobs_values.toarray()
# print(mother_jobs_values.shape)

'''SEX'''
sex_values=dataset['sex'].values
data_sex_labelEncoder = LabelEncoder()
sex_values=data_sex_labelEncoder.fit_transform(sex_values).reshape(-1,1)
# print(sex_values.shape)
#
'''Father JOB'''
father_jobs_values=dataset['Fjob'].values
data_father_job_labelEncoder = LabelEncoder()
data_father_job_labelOneHot =OneHotEncoder()
father_jobs_values=data_father_job_labelEncoder.fit_transform(father_jobs_values)
father_jobs_values =data_father_job_labelOneHot.fit_transform(np.reshape(father_jobs_values,(-1,1)))
father_jobs_values = father_jobs_values.toarray()
# print(father_jobs_values.shape)
#
#
'''Reason'''
reason_values=dataset['reason'].values
reason_job_labelEncoder = LabelEncoder()
data_reason_labelOneHot =OneHotEncoder()
reason_data_values=reason_job_labelEncoder.fit_transform(reason_values)
reason_data_values =data_reason_labelOneHot.fit_transform(np.reshape(reason_data_values,(-1,1)))
reason_data_values = reason_data_values.toarray()
# print(reason_data_values.shape)
#
'''schoolsup'''
schoolsup_values=dataset['schoolsup'].values
schoolsup_labelEncoder = LabelEncoder()
schoolsup_data_values=schoolsup_labelEncoder.fit_transform(schoolsup_values).reshape(-1,1)
# print(schoolsup_data_values.shape)
#
'''higher'''
higher_values=dataset['higher'].values
higher_labelEncoder = LabelEncoder()
higher_data_values=higher_labelEncoder.fit_transform(higher_values).reshape(-1,1)
# print(higher_data_values.shape)
#
#
'''Famsup'''
fams_values=dataset['famsup'].values
fams_labelEncoder = LabelEncoder()
fams_values=fams_labelEncoder.fit_transform(fams_values).reshape(-1,1)
# print(fams_values.shape)
#
column_age = dataset['age'].values.reshape(-1,1)
column_medu = dataset['Medu'].values.reshape(-1,1)
column_study_time = dataset['studytime'].values.reshape(-1,1)
column_goout = dataset['goout'].values.reshape(-1,1)
column_dalc = dataset['Dalc'].values.reshape(-1,1)
column_walc = dataset['Walc'].values.reshape(-1,1)
column_g1 = df['G1'].values.reshape(-1,1)
#

r1,r2,r3,r4 = np.split(reason_data_values, indices_or_sections=reason_data_values.shape[1], axis=1)
mj1,mj2,mj3,mj4,mj5 = np.split(mother_jobs_values, indices_or_sections=mother_jobs_values.shape[1], axis=1)
f1,f2,f3,f4,f5 = np.split(father_jobs_values, indices_or_sections=father_jobs_values.shape[1], axis=1)
X = np.concatenate((sex_values,column_age,column_medu, mj1,mj2,mj3,mj4,mj5,f1,f2,f3,f4,f5, r1,r2,r3,r4,column_study_time,
                    schoolsup_data_values,fams_values, higher_data_values, column_goout, column_dalc, column_walc, column_g1), axis=1)

# print("---------------------")
# print(mother_jobs_values.shape)
# print(father_jobs_values.shape)
# X = np.concatenate((sex_values,father_jobs_values.toarray(),mother_jobs_values.toarray()), axis=1)
# print(X.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=0)

# print(X_train.shape)
X_norm = StandardScaler()
X_train = X_norm.fit_transform(X_train)
# print(X_test.shape)
X_test = X_norm.transform(X_test)


######################
# Predict
###########################

def predictGradeTwo(data):
    age = data['age'].values.reshape(-1,1)
    medu = data['medu'].values.reshape(-1, 1)
    study_time = data['studytime'].values.reshape(-1, 1)
    goout = data['goout'].values.reshape(-1, 1)
    dalc = data['Dalc'].values.reshape(-1, 1)
    walc = data['Walc'].values.reshape(-1, 1)
    g1 = data['g1'].values.reshape(-1, 1)
    mjob = data_mother_job_labelEncoder.transform(data['mjob'].values)
    mjob = data_mother_job_labelOneHot.transform(np.reshape(mjob, (-1, 1)))
    mjob = mjob.toarray()
    # print(mjob.shape)

    fjob = data_father_job_labelEncoder.transform(data['fjob'].values)
    fjob = data_father_job_labelOneHot.transform(np.reshape(fjob, (-1, 1)))
    fjob = fjob.toarray()
    print(fjob.shape)

    reason = reason_job_labelEncoder.transform(data['reason'].values)
    reason = data_reason_labelOneHot.transform(np.reshape(reason, (-1, 1)))
    reason = reason.toarray()
    # print(reason.shape)


    '''schoolsup'''
    schoolsup = data['schoolsup'].values
    schoolsup_data_values = schoolsup_labelEncoder.transform(schoolsup).reshape(-1, 1)
    # print(schoolsup_data_values.shape)

    #
    '''higher'''
    higher = data['higher'].values
    higher_data_values = higher_labelEncoder.transform(higher).reshape(-1, 1)
    # print(higher_data_values.shape)
    #
    #
    '''Famsup'''
    fams = data['famsup'].values
    fams_values = fams_labelEncoder.transform(fams).reshape(-1, 1)
    # print(fams_values.shape)

    sex = data['sex'].values
    sex_values = data_sex_labelEncoder.transform(sex).reshape(-1, 1)
    print(sex_values.shape)

    r1, r2, r3, r4 = np.split(reason, indices_or_sections=reason.shape[1], axis=1)
    mj1, mj2, mj3, mj4, mj5 = np.split(mjob, indices_or_sections=mjob.shape[1], axis=1)
    f1, f2, f3, f4, f5 = np.split(fjob, indices_or_sections=fjob.shape[1], axis=1)


    try:
        X_test_new = np.concatenate((sex_values, age, medu, mj1, mj2, mj3, mj4, mj5, f1, f2, f3, f4, f5, r1, r2, r3, r4,
                                     study_time, schoolsup_data_values, fams_values,higher_data_values, goout, dalc, walc, g1), axis=1)
        # print(X_test_new.shape)
        X_test_new=X_norm.transform(X_test_new)
        filename = 'g2model.sav'
        g2model = pickle.load(open(filename, 'rb'))
        # val = np.reshape(X_test_new[1, 24], (1, -1))
        # print(val.shape)
        y_pred = g2model.predict(X_test_new)[0]
        print(y_pred)
        return y_pred
    except Exception as e:
        print(str(e))
        print("")






# # mlp = MLPRegressor(500,batch_size=28,solver='lbfgs', alpha=0.001, verbose=True, max_iter=1000, random_state=0)
# # mlp.fit(X_train, y_train)
# filename='g2model.sav'
# # pickle.dump(mlp, open(filename, 'wb'))
# # print(mlp.score(X_train, y_train))
# g2model = pickle.load(open(filename, 'rb'))
# val =np.reshape(X_test[1,:],(1,-1))
# print(val.shape)
# y_pred=g2model.predict(val)[0]
# print(y_pred)
# print(y_test[1])


