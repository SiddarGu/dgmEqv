
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']

# process data
data = {
    'Country': ['China', 'India', 'United States', 'Brazil', 'Russia'],
    'Total Land (Hectares)': [900000, 800000, 1000000, 900000, 1200000],
    'Arable Land (Hectares)': [400000, 300000, 500000, 450000, 600000],
    'Crop Land (Hectares)': [200000, 150000, 250000, 200000, 300000],
    'Fallow Land (Hectares)': [100000, 80000, 150000, 100000, 200000],
    'Permanent Crops (Hectares)': [100000, 90000, 120000, 80000, 150000],
    'Livestock (Number of Animals)': [5000000, 4000000, 6000000, 5000000, 8000000]
}
df = pd.DataFrame(data)
df.set_index('Country', inplace=True)

# create heatmap chart
fig, ax = plt.subplots(figsize=(12, 6))
heatmap = sns.heatmap(df, annot=True, fmt='g', cmap='RdBu_r', linewidths=0.5, cbar_kws={'label': 'Number of Animals'})

# set ticks and ticklabels
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)

# add title
ax.set_title('Agriculture and Livestock Distribution by Country')

# resize image and save
plt.tight_layout()
plt.savefig('./output/final/heatmap/png/20231228-155147_47.png', bbox_inches='tight')

# clear current image state
plt.clf()