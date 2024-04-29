import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Given data breakdown
data_labels = ["Daily Active Users (Million)"]
line_labels = ["Twotter", "Vumblr", "SnappyChat", "Pictograph", "LinkedOff", "InstaSnap"]
data = [np.mean([1.2, 2.4]), np.mean([2.5, 3.7]), np.mean([3.8, 5.0]), np.mean([5.1, 6.3]), np.mean([6.4, 7.6]), np.mean([7.7, 8.9])]

# Creating DataFrame from the given data
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Platform', 'Average Daily Active Users'])

# Create a figure and a grid of subplots
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plotting data
sns.barplot(x='Platform', y='Average Daily Active Users', data=df, ax=ax, palette="viridis")

# Set figure aesthetics
plt.title('Daily Active Users Comparison Amongst Social Media Platforms', fontsize=16)
plt.xlabel(data_labels[0], fontsize=14)
plt.ylabel('Average Users (Million)', fontsize=14)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust subplot params for a nicer fit
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/90.png'
if not os.path.exists(os.path.dirname(save_path)):
    os.makedirs(os.path.dirname(save_path))

plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure's state
plt.clf()
