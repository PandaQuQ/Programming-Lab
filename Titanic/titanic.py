import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import datasorting


#############################################################################
# Survival rates based on different factors (class, gender, age group)
#############################################################################

# Load the Titanic dataset
datasorting.sort_data()
titanic_data = pd.read_csv('titanic.csv')

# Calculate survival rates based on class
class_survival_rates = titanic_data.groupby('Pclass')['Survived'].mean()

# Calculate survival rates based on gender
gender_survival_rates = titanic_data.groupby('Sex')['Survived'].mean()

# Calculate survival rates based on age group
age_group_bins = [0, 18, 30, 50, 100]
age_group_labels = ['0-18', '19-30', '31-50', '51+']
titanic_data['AgeGroup'] = pd.cut(titanic_data['Age'], bins=age_group_bins, labels=age_group_labels)
age_group_survival_rates = titanic_data.groupby('AgeGroup')['Survived'].mean()

# Plot the survival rates
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
class_survival_rates.plot(kind='bar')
plt.title('Survival Rates by Class')
plt.xlabel('Class')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)

plt.subplot(1, 3, 2)
gender_survival_rates.plot(kind='bar')
plt.title('Survival Rates by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)

plt.subplot(1, 3, 3)
age_group_survival_rates.plot(kind='bar')
plt.title('Survival Rates by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.suptitle('Survival Rates Based on Different Factors', fontsize=16)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('Figure_1.png')
plt.show()

#############################################################################
#  Age distribution of passengers and passenger classes.
#############################################################################

# Calculate age distribution by passenger class
age_distribution_by_class = titanic_data.groupby('Pclass')['Age'].mean()

# Plot the age distribution by passenger class
plt.figure(figsize=(10, 6))
age_distribution_by_class.plot(kind='bar')
plt.title('Age Distribution by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Average Age')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('Figure_2.png')
plt.show()


#############################################################################
#  Age distribution of passengers according to passenger classes survived and genders.
#############################################################################

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
plt.scatter(x,y)
# create female part




# Show the plot
plt.savefig('Figure_3.png')
plt.show()


#############################################################################






#############################################################################
#  Relationship with Parch number and survival rate.
#############################################################################
# Calculate survival rates based on number of parents/children aboard
parch_survival_rates = titanic_data.groupby('Parch')['Survived'].mean()
# Plot the survival rates
plt.figure(figsize=(10, 6))
parch_survival_rates.plot(kind='bar')
plt.title('Survival Rates by Number of Parents/Children Aboard')
plt.xlabel('Number of Parents/Children Aboard')
plt.xticks(rotation=0)
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.savefig('Figure_4.png')
plt.show()

#############################################################################
#  Relationship with SibSp number and survival rate.
#############################################################################

