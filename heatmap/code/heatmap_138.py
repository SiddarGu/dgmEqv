
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data processing
categories = ['Search Engines', 'Social Media', 'E-commerce', 'Streaming Services', 'Online Gaming']
websites = [500, 700, 1000, 800, 600]
apps = [300, 500, 800, 600, 400]
devices = [100, 200, 500, 300, 200]
users = [1000, 2000, 5000, 3000, 2500]
data = [500, 1000, 2000, 1500, 1000]
internet_speed = [100, 200, 500, 300, 250]

# create dataframe
df = pd.DataFrame({'Category': categories,
                   'Number of Websites': websites,
                   'Number of Apps': apps,
                   'Number of Devices': devices,
                   'Number of Users': users,
                   'Amount of Data (PetaBytes)': data,
                   'Internet Speed (Mbps)': internet_speed})

# set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# plot heatmap
heatmap = sns.heatmap(df.set_index('Category'), cmap='Blues', annot=True, fmt='.0f', cbar=False, ax=ax)

# set tick labels and rotation
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation=0, ha='center')

# set title
ax.set_title('Technology and Internet Usage by Category')

# automatically resize and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_47.png', bbox_inches='tight')

# clear current image state
plt.clf()