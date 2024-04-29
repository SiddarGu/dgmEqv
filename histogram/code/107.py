import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Data
data_labels = ['Water', 'Petroleum', 'Natural Gas', 'Coal', 'Renewables', 'Nuclear']
data = [3200, 1800, 1500, 1200, 600, 400]
line_labels = ['Consumption (million metric tons)']

# Plot settings
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create vertical histogram
sns.barplot(x=data_labels, y=data, palette='viridis')

# Set title and labels
ax.set_title('Resource Consumption for Environmental and Sustainability Efforts', fontsize=16)
ax.set_xlabel('Type of Resource', fontsize=14)
ax.set_ylabel('Consumption (million metric tons)', fontsize=14)

# Rotate x-axis labels if too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=12, wrap=True)

# Automatically resize the image
plt.tight_layout()

# Save image to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/107.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current image state
plt.clf()
