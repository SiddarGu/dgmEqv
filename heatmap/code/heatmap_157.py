
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# define data as a dictionary
data = {'Country': ['United States', 'China', 'United Kingdom', 'Germany', 'France', 'Japan'],
        'Online Sales ($)': [200000000, 400000000, 300000000, 150000000, 100000000, 50000000],
        'In-Store Sales ($)': [500000000, 600000000, 400000000, 200000000, 200000000, 100000000],
        'Total Sales ($)': [700000000, 1000000000, 700000000, 350000000, 300000000, 150000000],
        'Online Sales (%)': [28, 40, 42.85, 42.85, 33.33, 33.33],
        'In-Store Sales (%)': [72, 60, 57.14, 57.14, 66.66, 66.66],
        'Total Sales (%)': [100, 100, 100, 100, 100, 100]}

# convert data to a pandas dataframe
df = pd.DataFrame(data)

# set the figure size
fig, ax = plt.subplots(figsize=(12, 8))

# plot the heatmap chart using seaborn
import seaborn as sns
sns.heatmap(df.iloc[:, 1:4], annot=True, fmt='.2f', cmap='Blues', cbar=False)

# set the x and y ticks and labels
ax.set_xticks(np.arange(3) + 0.5)
ax.set_yticks(np.arange(6) + 0.5)
ax.set_xticklabels(df.columns[1:4], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df['Country'])

# set the title of the figure
plt.title('E-commerce vs. In-Store Sales by Country')

# automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_81.png', bbox_inches='tight')

# clear the current image state
plt.clf()