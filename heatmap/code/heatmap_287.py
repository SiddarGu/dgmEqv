
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# data
data = {
    'Country': ['United States', 'Canada', 'United Kingdom', 'Germany', 'Japan', 'Australia', 'China', 'India', 'Brazil'],
    'Healthcare Expenditure (% of GDP)': [18, 12, 10, 14, 11, 17, 6, 5, 9],
    'Life Expectancy (years)': [75, 80, 82, 81, 84, 82, 76, 69, 75],
    'Physicians per 1000 People': [2.5, 2.2, 2.4, 2.6, 2.1, 2.3, 1.8, 1.2, 1.4],
    'Nurses per 1000 People': [3.8, 3.5, 3.2, 4.0, 3.1, 4.2, 2.4, 1.8, 2.2],
    'Beds per 1000 People': [2.9, 2.7, 2.6, 3.2, 2.5, 3.1, 1.9, 1.5, 1.8]
}

# convert data to dataframe
df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(10, 8))

# plot heatmap using seaborn
ax = sns.heatmap(df.drop('Country', axis=1), annot=True, cmap='Blues', cbar=False)

# set x and y ticks and ticklabels in the center
ax.set_xticks(np.arange(len(df.columns) - 1) + 0.5)
ax.set_yticks(np.arange(len(df)) + 0.5)
ax.set_xticklabels(df.drop('Country', axis=1).columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Country'], rotation=0, ha='right', rotation_mode='anchor')

# set title
ax.set_title('Comparison of Healthcare and Health Indicators by Country')

# resize image and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_23.png', bbox_inches='tight')

# clear current image state
plt.clf()