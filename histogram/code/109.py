import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Given data
data_labels = ['Number of Visitors (Thousands)']
line_labels = ['Contemporary Art', 'Classic Art', 'Modern Art', 'Sculpture', 'Photography', 'Digital Media']
data = [120, 95, 140, 80, 60, 50]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create the figure and the axes
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Create the vertical histogram
sns.barplot(x=df.index, y=df[data_labels[0]], ax=ax)

# Add title and labels
ax.set_title('Visitors Distribution Across Different Art Exhibition Types')
ax.set_ylabel('Number of Visitors (Thousands)')
ax.set_xlabel('Exhibition Type')

# Improve layout and aesthetics
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor', wrap=True)
sns.despine(bottom=True, left=True)
ax.grid(axis='y', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically resize the figure
plt.tight_layout()

# Create directories if not already present
output_dir = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png'
os.makedirs(output_dir, exist_ok=True)

# Save the figure
plt.savefig(f'{output_dir}/109.png', dpi=300)

# Clear the current image state
plt.clf()
