import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sklearn import datasets
import seaborn as sb
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv("Dataset/student_v1.csv")
# print(df)
df.dropna(axis=0, how='all')
# print(df)
df_y=df['G1']
df_x = df.drop(['address', 'famsize', 'Pstatus', 'Fedu', 'guardian', 'nursery'], axis=1)


def convert_to_01(x):
    x=x.lower()
    if x == "yes" or x == "m" or x == "ms":
        return 1
    elif x == "no" or x =="f" or x =="gp":
        return 0

def convert_to_01234(x):
    if x == "at_home" or x=="home":
        return 0
    elif x == "health" or x=="reputation":
        return 1
    elif x == "teacher" or x=="course":
        return 2
    elif x == "services":
        return 3
    else:
        return 4

df_schoolsup = df_x['schoolsup'].apply(convert_to_01)
df_famsup =  df_x['famsup'].apply(convert_to_01)
df_paid=df_x['paid'].apply(convert_to_01)
df_activities=df_x['activities'].apply(convert_to_01)
df_sex=df_x['sex'].apply(convert_to_01)
print(df_sex)
df_higher=df_x['higher'].apply(convert_to_01)
df_internet=df_x['internet'].apply(convert_to_01)
df_romantic=df_x['romantic'].apply(convert_to_01)
df_school=df_x['school'].apply(convert_to_01)
df_Mjob=df_x['Mjob'].apply(convert_to_01234)
df_Fjob=df_x['Fjob'].apply(convert_to_01234)
df_reason=df_x['reason'].apply(convert_to_01234)
df_x['schoolsup'] = df_schoolsup
df_x['famsup'] = df_famsup
df_x['paid']= df_paid
df_x['activities']=df_activities
df_x['sex']=df_sex
df_x['higher']=df_higher
df_x['internet']=df_internet
df_x['romantic']=df_romantic
df_x['school']=df_school
df_x['Mjob']=df_Mjob
df_x['Fjob']=df_Fjob
df_x['reason']=df_reason
# Scale
# scaler=MinMaxScaler()
# df_x = scaler.fit_transform(df_x,df_y)

data_frame=DataFrame(df_x)
df_x_set1 = df_x[['school','age','traveltime','famrel','sex','G1','G2','G3']]
df_x_set2 = df_x[['studytime','failures','schoolsup','famsup','G1','G2','G3']]
df_x_set3 = df_x[['activities','paid','higher','internet','G1','G2','G3']]
df_x_set4 = df_x[['romantic','freetime','goout','Medu', 'sex','Fjob','Mjob','reason', 'G1','G2','G3']]
df_x_set5 = df_x[['Dalc','Walc','health','absences','G1','G2','G3']]
print(df_x_set1.head())
# sb.heatmap(df_x_set1.corr(),annot=True)
# plt.show()

sb.heatmap(df_x_set5.corr(),annot=True)
plt.show()