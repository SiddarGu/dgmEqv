
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
data = {'Platform': ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Snapchat', 'TikTok'],
        'Number of Users (Millions)': [2000, 800, 500, 250, 200, 150],
        'Active Users (Millions)': [1500, 600, 400, 200, 150, 100],
        'Revenue (Millions)': [4000, 1200, 800, 600, 400, 300],
        'Ad Revenue (Millions)': [3500, 1100, 700, 500, 350, 250],
        'Monthly Visits (Millions)': [5000, 1500, 1000, 750, 500, 400]}

# Convert the data into a dataframe
df = pd.DataFrame(data)

# Set the index to Platform
df.set_index('Platform', inplace=True)

# Create the heatmap chart
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Value (Millions)'})

# Set the ticks and ticklabels for x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set the title and labels
ax.set_title('Social Media and Web Platform Metrics')
ax.set_xlabel('Metrics')
ax.set_ylabel('Platforms')

# Automatically resize the image and save it
fig.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-124154_20.png', bbox_inches='tight')

# Clear the current image state
plt.clf()