
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data_dict = {'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'], 'Income ($)': [50000, 55000, 48000, 52000], 'Expenses ($)': [40000, 45000, 37000, 38000], 'Profit ($)': [10000, 10000, 11000, 14000]}

# Convert first column to string type
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10,6))

# Use ax.stackplot() to plot area chart
ax = plt.axes()
ax.stackplot(df['Quarter'], df['Income ($)'], df['Expenses ($)'], df['Profit ($)'], labels=['Income', 'Expenses', 'Profit'], colors=['#66b3ff', '#ff9999', '#99ff99'], alpha=0.7)

# Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(0, len(df.index), 1))
    ax.set_xticklabels(df['Quarter'], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max()/1000)*1000)
    ax.set_yticks(np.linspace(0, ax.get_ylim()[1], np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(ls='--', lw=0.5)

# Set legend position
ax.legend(loc='upper left')

# Set title
plt.title('Quarterly Financial Performance')

# Automatically resize image and save as png
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_42.png', bbox_inches='tight')

# Clear current image state
plt.clf()