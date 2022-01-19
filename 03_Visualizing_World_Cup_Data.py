import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

## World Cup Matches Dataframe ##

df = pd.read_csv('WorldCupMatches.csv')
print(df.head())
# Create a new column and set it equal to the sum of the columns Home Team Goals and Away Team Goals
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())


## Bar chart ##

sns.set_context('poster', font_scale=0.8)
sns.set_style('whitegrid')
f, ax = plt.subplots(figsize=(20, 7))
ax = sns.barplot(x=df['Year'], y=df['Total Goals'])
ax.set_title('Average Number Of Goals Scored In World Cup Matches By Year')
plt.show()


## Goals Dataframe ##

df_goals = pd.read_csv('goals.csv')
print(df_goals.head())

## Box plot ##

sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(20, 7))
ax2 = sns.boxplot(data=df_goals, x='year', y='goals', palette='Spectral')
ax2.set_title('Goals Visualization')
plt.show()
