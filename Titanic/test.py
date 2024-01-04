import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

titanic_data = pd.read_csv('titanic.csv')

# Group data by passenger class, survival status, and gender
#grouped_data = titanic_data.groupby(['Pclass', 'Survived', 'Sex'])['Age'].mean().reset_index()
# Create separate dataframes for survived
grouped_data = titanic_data.loc[titanic_data['Survived'] == 1]
# Create new dataframes for each gender
df_male = grouped_data.loc[grouped_data['Sex'] == 'male']
df_female = grouped_data.loc[grouped_data['Sex'] == 'female']
# create male part
x = df_male['Age']
y = df_male['Pclass']
plt.scatter(x,y, color='blue',s=5)
# create female part
plt.show()
