import pandas as pd
'''
This function sorts the data in the titanic.csv file and saves it to titanic_sorted.csv.
'''
def sort_data():
    # Load the Titanic dataset
    df = pd.read_csv('titanic.csv', usecols=['PassengerId', 'Survived','Pclass','Name','Sex','Age','SibSp','Parch','Fare','Embarked'])
#    print(df.head())
    # Save the sorted data to a new file
    df.to_csv('titanic_sorted.csv', index=False)