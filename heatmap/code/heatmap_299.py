
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import and process data
data = {'Category': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Trucks (thousand)': [500, 200, 300, 400, 100, 150],
        'Ships (thousand)': [100, 50, 75, 80, 25, 30],
        'Trains (thousand)': [50, 25, 40, 45, 10, 20],
        'Planes (thousand)': [75, 40, 60, 70, 20, 30],
        'Pipelines (thousand)': [200, 100, 150, 180, 50, 75],
        'Barges (thousand)': [50, 25, 25, 40, 10, 15]}

df = pd.DataFrame(data)

# set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# plot heatmap using seaborn
sns.heatmap(df.iloc[:, 1:], annot=True, fmt='g', cmap='Blues', cbar=False)

# set ticks and tick labels for x and y axis
ax.set_xticks(np.arange(6) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticks(np.arange(6) + 0.5)
ax.set_yticklabels(df['Category'], rotation=0, ha='right', rotation_mode='anchor', wrap=True)

# add colorbar
cbar = ax.figure.colorbar(ax.collections[0])
cbar.set_label('Capacity (thousand)', rotation=270, labelpad=15)

# set title
plt.title('Transportation and Logistics Capacity by Region')

# adjust layout and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_35.png', bbox_inches='tight')

# clear figure state
plt.clf()