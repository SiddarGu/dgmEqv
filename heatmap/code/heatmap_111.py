
# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set data
data = {'2020': [2290, 2200, 1920, 1800, 1370],
        'Social Media Platform': ['YouTube', 'Facebook', 'Twitter', 'Instagram', 'Reddit']}

# Convert data into pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(12,8))

# Plot heatmap using seaborn
sns.heatmap(df.set_index('Social Media Platform'), annot=True, fmt='.0f', cmap='Blues')

# Set axis labels and ticks
plt.xlabel('Social Media Platform Users (Millions)', fontsize=12, labelpad=10)
plt.ylabel('Social Media Platform', fontsize=12, labelpad=10)
plt.xticks(rotation=45, ha='right', rotation_mode='anchor', fontsize=10)
plt.yticks(fontsize=10, va='center')

# Add title
plt.title('Social Media Platform Users in 2020', fontsize=14, pad=20)

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_12.png', bbox_inches='tight') 

# Clear current image state
plt.clf()