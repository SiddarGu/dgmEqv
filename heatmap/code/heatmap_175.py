

# import
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# data processing
data = {'Category': ['Social Media', 'Web'], 'Facebook (%)': [70, 30], 'Twitter (%)': [20, 80], 'Instagram (%)': [50, 50], 'LinkedIn (%)': [10, 90], 'YouTube (%)': [40, 60]}
df = pd.DataFrame(data)
df = df.set_index('Category')

# create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# plot heatmap
im = ax.imshow(df, cmap='RdYlGn_r', vmin=0, vmax=100)

# add colorbar
cbar = plt.colorbar(im, fraction=0.046, pad=0.04)

# set tick labels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))

# set tick positions
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index)

# set tick labels in the center
ax.tick_params(axis='both', which='both', labelsize=10)
plt.setp(ax.get_xticklabels(), ha="center", rotation_mode="anchor")

# show value in each cell
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha="center", va="center", color="w")

# add title
plt.title("Social Media and Web Usage Distribution")

# automatically resize image
plt.tight_layout()

# save figure
plt.savefig("output/final/heatmap/png/20231228-134212_28.png", bbox_inches='tight')

# clear current image state
plt.clf()