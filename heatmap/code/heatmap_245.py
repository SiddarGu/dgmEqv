


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set data
raw_data = {'Industry': ['Electricity Consumption (Billion kWh)', 'Renewable Energy Production (Billion kWh)', 'Natural Gas Consumption (Trillion cubic feet)', 'Coal Consumption (Million short tons)', 'Petroleum Consumption (Million barrels)'],
            'United States': [4000.5, 2000.2, 2500.8, 500.6, 100.2],
            'China': [3000.2, 1500.3, 3000.4, 400.5, 200.4],
            'Russia': [1000.7, 300.5, 2000.6, 300.2, 150.1],
            'Japan': [1500.2, 500.6, 500.5, 100.4, 50.2],
            'India': [2000.4, 1000.5, 1000.2, 200.3, 100.1],
            'Germany': [500.6, 250.1, 750.3, 150.2, 75.1]}

# convert data to dataframe
df = pd.DataFrame(raw_data, columns=['Industry', 'United States', 'China', 'Russia', 'Japan', 'India', 'Germany'])
df.set_index('Industry', inplace=True)

# set figure size
plt.figure(figsize=(12, 8))

# plot heatmap
ax = sns.heatmap(df, annot=True, cmap='RdBu_r', linewidths=0.5, fmt='.1f')

# set x and y ticks and labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='center')

# set title
plt.title('Energy Usage and Production by Country')

# resize image
plt.tight_layout()

# save figure
plt.savefig('output/final/heatmap/png/20231228-155147_42.png', bbox_inches='tight')

# clear image state
plt.clf()
plt.close()