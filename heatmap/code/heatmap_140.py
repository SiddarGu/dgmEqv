


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# create dictionary with the given data
data = {
    'Country': ['China', 'United States', 'India', 'Indonesia', 'Pakistan', 'Brazil'],
    'Population (Millions)': [1400, 328, 1350, 270, 220, 210],
    'Renewable Energy (%)': [15, 10, 20, 5, 3, 25],
    'Greenhouse Gas Emissions (Million Tons)': [3000, 5000, 2000, 1000, 800, 1500],
    'Forest Coverage (%)': [20, 30, 25, 50, 10, 60],
    'Water Quality (P)': [85, 90, 75, 65, 60, 80],
    'Air Quality (P)': [80, 85, 70, 60, 55, 75]
}

# convert dictionary to pandas dataframe
df = pd.DataFrame(data)

# set country column as index
df = df.set_index('Country')

# plot heatmap chart using seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(df, cmap='coolwarm', annot=True, cbar=False, fmt='g')
plt.title('Environmental Indicators by Country')
plt.yticks(rotation=0)
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.tick_params(axis='both', which='both', length=0, labelsize=10)
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_54.png', bbox_inches='tight')
plt.clf()

# clear current image state
plt.clf()