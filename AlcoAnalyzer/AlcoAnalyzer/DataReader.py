import numpy as np
import pandas as pd

dataset = pd.read_csv("Dataset/student.csv")
classes = dataset.Class
uniqueClasses = np.unique(classes.values)
print('Classes: '+classes)
print('UniqueClasses: '+uniqueClasses)