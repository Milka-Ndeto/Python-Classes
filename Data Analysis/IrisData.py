import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the Iris dataset from sklearn (or any dataset of your choice)
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Displaying the first few rows of the dataset
df.head()
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame (data=iris.data, columns=iris.feature_names)
# Check for missing values
print(df.isnull().sum())

# Check data types
print(df.dtypes)

#Cleaning the Data set
# Option 1: Drop missing values
df = df.dropna()

# Option 2: Fill missing values with the mean (if any)
# df = df.fillna(df.mean())

# Get basic statistics of numerical columns
print(df.describe())

# Group by species and compute the mean of numerical columns
species_group = df.groupby('species').mean()
print(species_group)

import seaborn as sns

# Bar plot for average petal length per species
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()

# Convert to a pandas DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add species labels from the 'target' attribute
species_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species'] = pd.Series(iris.target).map(species_names)

# Display the first few rows of the dataset
df.head()

# Count the occurrences of each species
df['species'].value_counts()

df.sample(10)

