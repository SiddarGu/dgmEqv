
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# process data
data = {'Area of Law': ['Personal Injury', 'Criminal Defense', 'Corporate Law', 'Family Law', 'Employment Law'],
        'Number of Cases Filed': [250, 150, 100, 200, 75],
        'Number of Cases Won': [175, 125, 90, 175, 50],
        'Average Settlement': [50000, 10000, 75000, 40000, 20000],
        'Number of Lawyers': [10, 8, 15, 12, 6],
        'Number of Clients': [200, 100, 50, 150, 75]}

df = pd.DataFrame(data)

# create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# plot heatmap
sns.heatmap(df[['Number of Cases Filed', 'Number of Cases Won', 'Average Settlement', 'Number of Lawyers', 'Number of Clients']], cmap='Blues', annot=True, fmt='d', cbar=False)

# set x and y tick labels
ax.set_xticklabels(df['Area of Law'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Area of Law'], rotation=0, ha='center')

# set title
plt.title('Legal Metrics by Area of Law')

# resize and save image
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231225-210514_48.png', bbox_inches='tight')

# clear current image state
plt.clf()