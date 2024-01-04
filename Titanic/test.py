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

#############################################################################
#  Relationship between age and fare.
#############################################################################

# Create a scatter plot of age vs. fare
plt.scatter(titanic_data['Age'], titanic_data['Fare'],color='#E81981')
#plt.arrow(20, 400, 14, 100, head_width=1, head_length=2, fc='#FFDB5D',ec='#FFDB5D')
plt.annotate('Outliers',xy=(34,500),xytext=(20,400),
             arrowprops={"width":2,"headwidth":10,'headlength':10,'color':'#FFDB5D'},
             horizontalalignment='center',fontsize=15)
plt.title('Age vs. Fare',font = fpath)
plt.xlabel('Age',font= fpath)
plt.ylabel('Fare',font= fpath)
plt.xticks(rotation=0,font= fpath)
plt.yticks(font= fpath)
plt.tight_layout()
plt.savefig('Figure_test.png',transparent=True)
plt.show()
