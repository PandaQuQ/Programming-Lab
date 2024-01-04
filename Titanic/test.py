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

print('A')

#############################################################################
# Survival rates based on different factors (class, gender, age group)
#############################################################################

# Sort the Titanic dataset
# Load the Titanic dataset
df = pd.read_csv('titanic.csv', usecols=['PassengerId', 'Survived','Pclass','Name','Sex','Age','SibSp','Parch','Fare','Embarked'])
# Save the sorted data to a new file
df.to_csv('titanic_sorted.csv', index=False)

# Load the sorted Titanic dataset
titanic_data = pd.read_csv('titanic_sorted.csv')

class_survival = titanic_data.groupby('Pclass')['Survived'].mean()

class_genders = titanic_data.groupby(['Pclass', 'Sex']).size().unstack()

# Plotting survival rates by class
plt.bar(class_survival.index, class_survival, color=['#FFDB5D','#94EE6B','#E81981'])
plt.title('Survival Rates by Class',font=fpath)
plt.xlabel('Passenger Class',font=fpath)
plt.ylabel('Survival Rate',font=fpath)
plt.xticks(rotation=0,font=fpath)
plt.yticks(font=fpath)
plt.savefig('test.png', transparent=True)
plt.show()

# Plotting genders by class
class_genders.plot(kind='bar', stacked=True, color=['#E81981','#FFDB5D'])
plt.title('Genders by Class',font=fpath)
plt.xlabel('Passenger Class',font=fpath)
plt.ylabel('Count',font=fpath)
plt.xticks(rotation=0,font=fpath)
plt.yticks(font=fpath)
plt.savefig('test2.png', transparent=True)
plt.show()