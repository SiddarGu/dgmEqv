import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Data preprocessing
data_labels = ["Active Users (Millions)"]
line_labels = [
    "Facebook", "YouTube", "Instagram", "Twitter", 
    "Snapchat", "Pinterest", "LinkedIn", "TikTok", "Reddit"
]
data = [
    320, 250, 200, 150, 
    120, 115, 95, 80, 75
]

# Prepare DataFrame for Seaborn
df = pd.DataFrame(data=np.array(data).reshape(-1, 1), index=line_labels, columns=data_labels)

# Creating the figure
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plotting
sns.barplot(
    x=df.index, y=df["Active Users (Millions)"], 
    palette="viridis", ax=ax
)

# Add title and labels
ax.set_title('Active User Statistics Across Major Social Media Platforms')
ax.set_xlabel('Social Media Platform')
ax.set_ylabel('Active Users (Millions)')

# Improve the appearance
plt.xticks(rotation=45, ha='right', wrap=True)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save Figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/191.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
