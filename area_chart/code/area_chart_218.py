

{'Platform': ['Facebook', 'Instagram', 'Twitter', 'TikTok', 'YouTube'], 'Likes': [23000, 7000, 12000, 10000, 8000], 'Comments': [1000, 2000, 800, 500, 700], 'Shares': [500, 800, 300, 200, 400]}


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Convert data to dictionary and process data using pandas
data = {'Platform': ['Facebook', 'Instagram', 'Twitter', 'TikTok', 'YouTube'], 'Likes': [23000, 7000, 12000, 10000, 8000], 'Comments': [1000, 2000, 800, 500, 700], 'Shares': [500, 800, 300, 200, 400]}
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create axes
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

# Set colors and transparency
colors = ['#3572D2', '#F56040', '#1DA1F2', '#000000', '#FF0000']
alpha = 0.7

# Plot area chart using ax.stackplot()
ax.stackplot(df.index, df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=['Likes', 'Comments', 'Shares'], colors=colors, alpha=alpha)

# Set ticks and ticklabels for x-axis
ax.set_xticks(df.index)
ax.set_xticklabels(df['Platform'], rotation=45, ha='right', rotation_mode='anchor')

# Set ticks and ticklabels for y-axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/1000)*1000 # Round up to nearest multiple of 1000
y_ticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(y_ticks)

# Set grid lines
ax.grid(color='grey', linestyle='--')

# Set legend position and labels
ax.legend(loc='upper left')
ax.set_ylabel('Engagement')
ax.set_xlabel('Platform')

# Set title
ax.set_title('Social Media Engagement by Platform')

# Automatically resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_61.png', bbox_inches='tight')

# Clear current image state
plt.clf()
plt.close()