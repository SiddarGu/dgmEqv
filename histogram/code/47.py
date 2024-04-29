import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Given data
data_labels = ['Number of Shipments (Thousands)']
line_labels = ['Consumer Goods', 'Industrial Products', 'Agricultural Products', 'Electronic Goods',
               'Pharmaceuticals', 'Textiles', 'Chemical Products', 'Machinery and Equipment']
data = [250, 200, 150, 180, 120, 130, 140, 160]

# Create dataframe
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Set the figure size
plt.figure(figsize=(10, 8))

# Create a subplot
ax = plt.subplot()

# Create histogram
sns.barplot(x=df.index, y=df[data_labels[0]], ax=ax, palette='viridis')

# Set title
ax.set_title('Volume of Shipments by Cargo Type in Transportation and Logistics Industry')

# Rotate x-axis labels if they are too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# Set the background grid
ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5, color='gray')

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/47.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
