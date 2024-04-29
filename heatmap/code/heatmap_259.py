
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Process data using dict and pandas
data = {'Platform': ['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'TikTok', 'Snapchat'],
        'North America': [60, 40, 55, 30, 45, 35],
        'Europe': [50, 35, 40, 25, 30, 22],
        'Asia': [40, 30, 35, 20, 28, 20],
        'South America': [25, 20, 22, 18, 18, 15],
        'Africa': [18, 15, 12, 10, 8, 7],
        'Oceania': [10, 8, 5, 3, 5, 3]}

df = pd.DataFrame(data)
df = df.set_index('Platform')

# Plot heatmap chart using ax and imshow()
fig, ax = plt.subplots(figsize=(10,8))
im = ax.imshow(df, cmap='Blues')

# Add ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df.index)))
ax.set_yticklabels(df.index)

# Add colorbar and title
cb = fig.colorbar(im)
plt.title('Social Media Usage by Region')

# Automatically resize and save image
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_6.png', bbox_inches='tight')

# Clear current image state
plt.clf()