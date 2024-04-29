

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# create dictionary with data
data = {'City': ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'House Price ($)': [500000, 450000, 300000, 250000, 200000],
        'Rent Price ($)': [3000, 2500, 2000, 1800, 1500],
        'Vacancy Rate (%)': [5, 5, 6, 7, 8],
        'Affordability Index': [60, 65, 70, 75, 80],
        'Homeownership Rate (%)': [50, 55, 60, 65, 70]}

# convert dictionary to pandas dataframe
df = pd.DataFrame(data)

# set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# create heatmap plot
heatmap = sns.heatmap(df[['House Price ($)', 'Rent Price ($)', 'Vacancy Rate (%)', 'Affordability Index', 'Homeownership Rate (%)']].corr(), 
                      annot=True, 
                      linewidths=0.5, 
                      cmap='coolwarm', 
                      cbar=False, 
                      annot_kws={'size': 12})

# set tick labels and positions
ax.set_xticklabels(['House Price ($)', 'Rent Price ($)', 'Vacancy Rate (%)', 'Affordability Index', 'Homeownership Rate (%)'], rotation=45, ha='right')
ax.set_yticklabels(['House Price ($)', 'Rent Price ($)', 'Vacancy Rate (%)', 'Affordability Index', 'Homeownership Rate (%)'], rotation=0, ha='right')

# set tick positions to center
ax.set_xticks(np.arange(0.5, 5.5))
ax.set_yticks(np.arange(0.5, 5.5))

# set title
ax.set_title('Housing Market Comparison in Major Cities')

# automatically resize and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_16.png', bbox_inches='tight')

# clear figure
plt.clf()