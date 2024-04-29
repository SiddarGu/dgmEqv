

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# import data and convert to dictionary
data = {'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Electricity Consumption (GWh)': [200000, 100000, 150000, 300000, 50000, 50000],
        'Natural Gas Consumption (MMcf)': [30000, 15000, 20000, 40000, 8000, 10000],
        'Petroleum Consumption (Barrels)': [100000, 50000, 80000, 200000, 25000, 30000],
        'Renewable Energy Consumption (GWh)': [50000, 25000, 40000, 100000, 12000, 15000]
        }

# create dataframe from dictionary
df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(10, 8))

# create heatmap using seaborn
ax = sns.heatmap(data=df.set_index('Region'), annot=True, fmt='g')
ax.set_title('Energy Consumption by Region')

# set ticks and labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='right', rotation_mode='anchor')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231226-140552_13.png', bbox_inches='tight')

# clear current image state
plt.clf()