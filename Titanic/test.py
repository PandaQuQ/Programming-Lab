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
plt.title('Survival Rates by Class')
plt.xlabel('Class')
plt.ylabel('Survival Rate')

# Adding percentage labels to the survival rates by class 
for p in plt.gca().containers:
    plt.gca().bar_label(p, color='white', fmt='%.2f%%')
    
plt.savefig('Figure_12.png', transparent=True)
plt.show()


# Plotting genders by class
class_genders.plot(kind='barh', stacked=True, color=['#FFDB5D','#E81981'])
plt.title('Genders by Class')
plt.xlabel('Count')
plt.ylabel('Class')

# Adding percentage labels to the genders by class 
for p in plt.gca().containers:
    plt.gca().bar_label(p, color='white', fmt='%.1f%%')

plt.savefig('Figure_13.png', transparent=True)
plt.show()