import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

animals = pd.read_csv('SleepInMammals.csv')
animals['Body Weight (kg)_log'] = np.log1p(animals['Body Weight (kg)'])
animals['Brain Weight (g)_log'] = np.log1p(animals['Brain Weight (g)'])
column_mapping = {
    'Species of animal': 'species',
    'Maximum life span (years)': 'age'
    }
animals.rename(columns=column_mapping, inplace=True)
# animals.head()
# animals.info()
# column_mapping = {
# 'Species of animal': 'species',
# 'Maximum life span (years)': 'age'
# #'old_name2': 'new_name2',
# # Add more mappings as needed
# }
# # Rename the columns using the rename method
# animals.rename(columns=column_mapping, inplace=True)
# print(animals['species'])

# Visual inspection - histogram and horizontal boxplot of log-transformed
fig, axes = plt.subplots(3, 2, figsize=(12, 12))
axes[0,0].hist(animals['Body Weight (kg)_log'],bins=20)
axes[0,0].set_title('Histogram: Log-transformed Body Weight')
axes[0,0].set_xlabel('Log-transformed Body Weight (kg)')

axes[0,1].hist(animals['Brain Weight (g)_log'],bins=20)
axes[0,1].set_title('Histogram: Log-transformed Brain Weight')
axes[0,1].set_xlabel('Log-transformed Brain Weight (g)')


axes[1,0].boxplot(animals['Body Weight (kg)_log'], vert=False)
axes[1,0].set_title('Boxplot: Log-transformed Body Weight')

axes[1,1].boxplot(animals['Brain Weight (g)_log'], vert=False)
axes[1,1].set_title('Boxplot: Log-transformed Brain Weight')

axes[2,0].scatter(animals['Body Weight (kg)_log'], animals['Brain Weight (g)_log'])
axes[2,0].set_xlabel('Log-transformed Body Weight (kg)')
axes[2,0].set_ylabel('Log-transformed Brain Weight (g)')
axes[2,0].set_title('Scatterplot: Log-transformed Brain Weight vs. Log-transformed Body Weight')
axes[2,0].grid(True)
for i,animal in animals.iterrows():
    axes[2,0].text(animal['Body Weight (kg)_log'], animal['Brain Weight (g)_log'], animal['species'],
                   fontsize=8, ha='right')

print(type(animals))

plt.tight_layout()
plt.show()
