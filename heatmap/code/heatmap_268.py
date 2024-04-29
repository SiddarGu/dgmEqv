
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# process the data
data = {'Year': [2021, 2022, 2023, 2024, 2025],
        'Domestic Visitors (in millions)': [125, 130, 135, 140, 145],
        'International Visitors (in millions)': [26, 28, 30, 32, 34],
        'Revenue ($ in billions)': [220, 230, 240, 250, 260],
        'Hotel Occupancy Rate (%)': [70, 72, 74, 76, 78],
        'Airbnb Occupancy Rate (%)': [80, 82, 84, 86, 88]}

df = pd.DataFrame(data)
df = df.set_index('Year')

# plot the chart
fig, ax = plt.subplots(figsize=(10,8))

# plot the heatmap using sns.heatmap()
sns.heatmap(df, annot=True, cmap='Blues', fmt='g', ax=ax)

# set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns))+0.5)
ax.set_yticks(np.arange(len(df.index))+0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# add colorbar
cbar = ax.collections[0].colorbar
cbar.set_ticks(np.arange(0, 300, 50))
cbar.set_ticklabels(np.arange(0, 300, 50))

# set title
plt.title('Tourism and Hospitality Metrics')

# resize and save the image
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-162116_23.png', bbox_inches='tight')

# clear image state
plt.clf()