
# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import seaborn as sns

# set data
data = {'Product': ['Wheat', 'Corn', 'Rice', 'Soybeans', 'Barley', 'Potatoes'],
        'Cost per Pound ($)': [0.15, 0.20, 0.10, 0.25, 0.12, 0.08],
        'Production Volume (lbs)': [50000, 75000, 25000, 100000, 40000, 75000],
        'Market Share (%)': [5, 8, 3, 10, 4, 10],
        'Unit Price ($)': [1.50, 2.00, 0.75, 2.50, 1.00, 0.75],
        'Revenue ($)': [75000, 150000, 18750, 250000, 40000, 56250],
        'Profit ($)': [25000, 60000, 6250, 100000, 16000, 18750]
        }

# convert data to pandas dataframe
df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(12, 8))

# create heatmap chart
ax = sns.heatmap(df.set_index('Product'), annot=True, cmap='RdYlGn', linewidths=0.5)

# set x and y axis ticks and ticklabels
# ax.set_xticks(np.arange(len(df.columns)))
# ax.set_yticks(np.arange(len(df.columns)))
# ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
# ax.set_yticklabels(df.columns, rotation=0, ha='right', rotation_mode='anchor')

# set title
plt.title('Crop Production and Profit in the Food and Beverage Industry')

# automatically resize image
plt.tight_layout()

# save image
plt.savefig('output/final/heatmap/png/20231228-124154_74.png', bbox_inches='tight')

# clear current image state
plt.clf()