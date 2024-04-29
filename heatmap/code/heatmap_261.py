
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns

# import data
data = {
    'Platforms': ['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'Pinterest', 'Tumblr'],
    'Number of Users (Millions)': [2340, 1410, 1300, 1060, 900, 800]
}


# create pandas dataframe
df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(12,8))

# create heatmap chart using seaborn
ax = sns.heatmap(df.set_index('Platforms'),
                 cmap='Blues', annot=True, fmt='g', linewidths=0.5, cbar=False)

# set tick labels and positions
# ax.set_xticks(np.arange(0.5, 6.5, 1))
# ax.set_xticklabels(df['2019'], rotation=45, ha='right', rotation_mode='anchor')
# ax.set_yticks(np.arange(0.5, 6.5, 1))
# ax.set_yticklabels(df['Social Media Platform'], rotation=0, ha='right', rotation_mode='anchor')

# set title
plt.title('Social Media Platform Usage')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_9.png', bbox_inches='tight')

# clear current image state
plt.clf()