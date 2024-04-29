
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Import seaborn for heatmap
import seaborn as sns

data = {'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Education Spending (Billion USD)': [500, 200, 600, 800, 100, 200],
        'Healthcare Spending (Billion USD)': [800, 400, 900, 1000, 200, 300],
        'Infrastructure Spending (Billion USD)': [400, 300, 500, 600, 100, 150],
        'Social Services Spending (Billion USD)': [300, 200, 400, 500, 50, 100],
        'Military Spending (Billion USD)': [100, 50, 200, 300, 25, 50]}

#Convert data to dataframe
df = pd.DataFrame(data)

#Set region as index
df.set_index('Region', inplace=True)

#Create heatmap chart using seaborn
fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(df, annot=True, fmt='g', cmap='Blues', cbar=True)
plt.title('Government Spending by Region')
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_69.png', bbox_inches='tight')
plt.close(fig)
