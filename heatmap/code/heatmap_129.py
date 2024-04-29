
# import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create dictionary with data
data_dict = {
    'Country': ['China', 'United States', 'Japan', 'Germany', 'South Korea'],
    'Steel Production (Million Tonnes)': [850, 500, 400, 350, 300],
    'Chemical Production (Million Tonnes)': [750, 450, 350, 300, 250],
    'Automobile Production (Million Units)': [35, 15, 8, 10, 6],
    'Pharmaceutical Production (Million Units)': [850, 400, 300, 250, 200],
    'Textile Production (Million Tonnes)': [500, 300, 200, 150, 100],
    'Paper Production (Million Tonnes)': [600, 400, 250, 200, 150]
}

# convert data into pandas dataframe
data_df = pd.DataFrame(data_dict)

# set country as index
data_df.set_index('Country', inplace=True)

# create heatmap chart using seaborn
import seaborn as sns

# set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# plot heatmap using seaborn
sns.heatmap(data_df, annot=True, cmap='Blues', cbar=False)

# set x and y tick labels in the center
ax.set_xticklabels(data_df.columns, ha='center', rotation=45, rotation_mode='anchor')
ax.set_yticklabels(data_df.index, va='center')

# set title
plt.title('Production Output by Country in Manufacturing')

# automatically resize image
plt.tight_layout()

# save figure
plt.savefig('output/final/heatmap/png/20231228-131639_35.png', bbox_inches='tight')

# clear current image state
plt.clf()