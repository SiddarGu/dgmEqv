
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# create dataframe
data = {'Category': ['Football', 'Basketball', 'Baseball', 'Hockey', 'Soccer', 'Tennis'],
        'Revenue (Millions)': [350, 250, 200, 150, 300, 100],
        'Fan Engagement (Millions)': [200, 150, 100, 75, 175, 50],
        'Social Media Followers (Millions)': [150, 100, 75, 50, 125, 25],
        'Ticket Sales (Millions)': [225, 175, 125, 100, 200, 75],
        'Merchandise Sales (Millions)': [100, 75, 50, 25, 75, 25],
        'Sponsorship Revenue (Millions)': [175, 150, 100, 75, 150, 50]}

df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(10,8))

# create heatmap
ax = sns.heatmap(df.set_index('Category'), cmap='YlGnBu', annot=True, fmt="g", linewidths=0.5, cbar=False)

# set x and y ticks
ax.set_xticklabels(ax.get_xticklabels(), ha='right', rotation=45, rotation_mode='anchor', wrap=True, fontsize=12)
ax.set_yticklabels(ax.get_yticklabels(), ha='right', rotation=45, rotation_mode='anchor', wrap=True, fontsize=12)

# set ticks and ticklabels to be in the center
plt.tick_params(axis='both', which='both', bottom=False, left=False)
ax.set_xticks(np.arange(0.5, 6.5, 1))
ax.set_yticks(np.arange(0.5, 6.5, 1))

# add title
plt.title('Sports and Entertainment Industry Metrics', fontsize=16, pad=20)

# resize and save image
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_28.png', bbox_inches='tight')

# clear current image state
plt.clf()
plt.cla()
plt.close()