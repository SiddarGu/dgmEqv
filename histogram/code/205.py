import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Data preprocessing
data_labels = ['Volume (million metric tons)']
line_labels = ['Road', 'Rail', 'Water', 'Air', 'Pipeline']
data = np.array([2500, 1400, 900, 300, 500])

# Create a DataFrame for ease of use with seaborn
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Setup the matplotlib figure and axes
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Create the histogram
sns.barplot(x=df.index, y=df[data_labels[0]], ax=ax, palette="viridis")

# Set the title and labels of the figure
ax.set_title('Annual Freight Volume by Transportation Mode', fontsize=16)
ax.set_ylabel('Volume (million metric tons)', fontsize=12)
ax.set_xlabel('Freight Method', fontsize=12)

# Rotate labels if they are too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", wrap=True)

# Change edge color and linewidth
for container in ax.containers:
    plt.setp(container, linewidth=1.5, edgecolor='k')

# Ensure the image content is not cut off
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/205.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, dpi=300)

# Clear the current figure's state to prevent overlay of figures
plt.clf()
