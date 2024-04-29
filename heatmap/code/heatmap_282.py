
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# initialize data
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Median Sale Price ($)': [500000, 450000, 350000, 300000, 250000],
        'Median Rental Price ($)': [2500, 2000, 1800, 1500, 1300],
        'Average Mortgage Rate (%)': [3.2, 3.5, 3.8, 4.0, 4.2],
        'Average Property Tax (%)': [2.5, 2.2, 2.0, 1.8, 1.5],
        'Average Home Insurance (%)': [1.8, 1.5, 1.2, 1.0, 0.8]}

# create dataframe
df = pd.DataFrame(data)

# set City as index
df = df.set_index('City')

# plot heatmap
fig, ax = plt.subplots(figsize=(12,8))
heatmap = ax.imshow(df, cmap='RdYlGn')

# add x-axis and y-axis ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns, fontsize=12, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, fontsize=12)

# center ticks and ticklabels
ax.tick_params(axis='both', which='both', length=0)
ax.tick_params(axis='x', pad=10)

# add value labels for each cell
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='black', size=12)

# add colorbar
fig.colorbar(heatmap)

# add title
plt.title('Key Real Estate Metrics in Major Cities', fontsize=16)

# resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_18.png', bbox_inches='tight')

# clear image state
plt.clf()