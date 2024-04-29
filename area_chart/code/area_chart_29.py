
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# represent the data using a dictionary
data = {'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G', 'Product H', 'Product I', 'Product J'], 'Total Production (Units)': [5000, 8000, 6000, 7000, 9000, 4000, 6500, 5500, 7500, 8500], 'Defects (Units)': [100, 150, 200, 120, 180, 100, 140, 130, 160, 190], 'Scrap (Units)': [200, 300, 250, 150, 200, 150, 180, 170, 200, 250], 'Waste (Units)': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Rejections (Units)': [50, 100, 70, 60, 80, 40, 50, 60, 80, 90]}

# use pandas to process the data
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# plot the data with the type of area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df.index, df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Total Production', 'Defects', 'Scrap', 'Waste', 'Rejections'], colors=['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD'], alpha=0.7)

# randomly set background grid lines
ax.grid(alpha=0.3)

# set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df['Product'], rotation=45, ha='right', rotation_mode='anchor')
if np.random.choice([True, False], p=[0.7, 0.3]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# set legend's position
ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1), borderaxespad=0)

# automatically resize the image
fig.tight_layout()

# set title and labels
ax.set_title('Production and Defects by Product')
ax.set_xlabel('Product')
ax.set_ylabel('Units')

# save the image
fig.savefig('output/final/area_chart/png/20231226-130527_14.png', bbox_inches='tight')

# clear the current image
plt.clf()