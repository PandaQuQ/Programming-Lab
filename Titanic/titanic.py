import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#############################################################################
# Survival rates based on different factors (class, gender, age group)
#############################################################################

# Sort the Titanic dataset
# Load the Titanic dataset
df = pd.read_csv('titanic.csv', usecols=['PassengerId', 'Survived','Pclass','Name','Sex','Age','SibSp','Parch','Fare','Embarked'])
#    print(df.head())
# Save the sorted data to a new file
df.to_csv('titanic_sorted.csv', index=False)

# Load the sorted Titanic dataset
titanic_data = pd.read_csv('titanic_sorted.csv')

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

# Show the plot
plt.savefig('Figure_3.png')
plt.show()

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
# average fare for each passenger class
#############################################################################
# Calculate average fare for each passenger class
average_fare = titanic_data.groupby('Pclass')['Fare'].mean()
# Plot the average fare
plt.figure(figsize=(10, 6))
average_fare.plot(kind='bar')
plt.title('Average Fare by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Average Fare')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('Figure_5.png')
plt.show()

#############################################################################
#  Relationship between age and fare.
#############################################################################

# Create a scatter plot of age vs. fare
plt.scatter(titanic_data['Age'], titanic_data['Fare'])
plt.title('Age vs. Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.tight_layout()
plt.savefig('Figure_6.png')
plt.show()

#############################################################################
#  Average survivor age by passenger class.
#############################################################################

# Calculate average survivor age by passenger class
grouped_data = titanic_data.loc[titanic_data['Survived'] == 1]
average_survivor_age = grouped_data.groupby('Pclass')['Age'].mean()
# Plot the average survivor age
plt.figure(figsize=(10, 6))
average_survivor_age.plot(kind='bar')
plt.title('Average Survivor Age by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Average Survivor Age')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('Figure_7.png')
plt.show()

#############################################################################
#  Average death age by passenger class.
#############################################################################

# Calculate average death age by passenger class
grouped_data = titanic_data.loc[titanic_data['Survived'] == 0]
average_death_age = grouped_data.groupby('Pclass')['Age'].mean()
# Plot the average death age
plt.figure(figsize=(10, 6))
average_death_age.plot(kind='bar')
plt.title('Average Death Age by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Average Death Age')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('Figure_8.png')
plt.show()

#############################################################################
#   Pie chart of passenger class distribution.
#############################################################################

# Calculate passenger class distribution
passenger_class_distribution = titanic_data['Pclass'].value_counts()
# Plot the passenger class distribution
plt.figure(figsize=(10, 6))
passenger_class_distribution.plot(kind='pie', autopct='%.2f%%')
plt.title('Passenger Class Distribution')
plt.tight_layout()
plt.savefig('Figure_9.png')
plt.show()

#############################################################################
#   Pie chart of passenger embarkation port distribution.
#############################################################################

# Calculate passenger embarkation port distribution
passenger_embarkation_port_distribution = titanic_data['Embarked'].value_counts()
# Plot the passenger embarkation port distribution
plt.figure(figsize=(10, 6))
passenger_embarkation_port_distribution.plot(kind='pie', autopct='%.2f%%')
plt.title('Passenger Embarkation Port Distribution')
plt.tight_layout()
plt.savefig('Figure_10.png')
plt.show()

#############################################################################
#   Pie chart of sex distribution.
#############################################################################

# Calculate passenger sex distribution
passenger_sex_distribution = titanic_data['Sex'].value_counts()
# Plot the passenger sex distribution
plt.figure(figsize=(10, 6))
passenger_sex_distribution.plot(kind='pie', autopct='%.2f%%')
plt.title('Passenger Sex Distribution')
plt.tight_layout()
plt.savefig('Figure_11.png')
plt.show()

#############################################################################
#   Gender distribution by passenger class.
#   Stella's code
#############################################################################

class_genders = titanic_data.groupby(['Pclass', 'Sex']).size().unstack()
# Plotting genders by class
class_genders.plot(kind='bar', stacked=True)
plt.title('Genders by Class')
plt.xlabel('Class')
plt.ylabel('Count')
plt.savefig('Genders by Class')
plt.savefig('Figure_12.png')
plt.show()