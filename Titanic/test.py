import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager
from pathlib import Path
import matplotlib as mpl


matplotlib.font_manager.findSystemFonts(fontpaths='./Fonts', fontext='ttf')
fpath = Path("Fonts/Quantico-Regular.ttf")
COLOR = 'white'
mpl.rcParams['text.color'] = COLOR
mpl.rcParams['axes.labelcolor'] = COLOR
mpl.rcParams['xtick.color'] = COLOR
mpl.rcParams['ytick.color'] = COLOR


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
class_survival_rates.plot(kind='bar',color='#FFDB5D')
plt.title('Survival Rates by Class',font= fpath)
plt.xlabel('Class',font = fpath)
plt.ylabel('Survival Rate',font = fpath)
plt.xticks(rotation=0,font = fpath)
plt.yticks(font = fpath)

plt.subplot(1, 3, 2)
gender_survival_rates.plot(kind='bar',color='#94EE6B')
plt.title('Survival Rates by Gender',font= fpath)
plt.xlabel('Gender',font = fpath)
plt.ylabel('Survival Rate',font = fpath)
plt.xticks(rotation=0,font = fpath)
plt.yticks(font = fpath)

plt.subplot(1, 3, 3)
age_group_survival_rates.plot(kind='bar',color='#E81981')
plt.title('Survival Rates by Age Group',font = fpath)
plt.xlabel('Age Group',font = fpath)
plt.ylabel('Survival Rate',font = fpath)
plt.suptitle('Survival Rates Based on Different Factors', fontsize=16,font = fpath)
plt.xticks(rotation=0,font = fpath)
plt.yticks(font = fpath)
#plt.tight_layout()
plt.savefig('Figure_test.png',transparent=True)
plt.show()