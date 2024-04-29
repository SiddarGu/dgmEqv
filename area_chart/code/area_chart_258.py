
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a dictionary to store the data
data = {'Category': ['Taxation', 'Social Welfare', 'Public Transportation', 'Law Enforcement', 'Environment Protection', 'Education', 'National Security', 'Foreign Policy', 'Emergency Services', 'Housing', 'Civil Rights', 'Healthcare', 'Social Services', 'Immigration'],
        'Healthcare (%)': [20, 30, 10, 25, 10, 15, 20, 25, 15, 20, 25, 15, 20, 25],
        'Education (%)': [15, 25, 15, 15, 20, 30, 10, 10, 20, 15, 20, 25, 15, 10],
        'Infrastructure (%)': [25, 20, 30, 20, 15, 20, 15, 15, 25, 20, 15, 20, 25, 20],
        'Security (%)': [15, 15, 25, 30, 25, 15, 30, 20, 20, 25, 20, 15, 20, 20],
        'Environment (%)': [25, 10, 20, 10, 30, 20, 25, 30, 20, 20, 20, 25, 20, 25]}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Use ax.stackplot() to plot the data as an area chart
ax.stackplot(df['Category'], df['Healthcare (%)'], df['Education (%)'], df['Infrastructure (%)'], df['Security (%)'], df['Environment (%)'], labels=['Healthcare', 'Education', 'Infrastructure', 'Security', 'Environment'], colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8)

# Set the background grid lines
ax.grid(color='grey', linestyle=':', linewidth=0.5)

# Set the x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set the rotation and wrap for the x and y ticks' label
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32), rotation=0, ha='right', rotation_mode='anchor', wrap=True)

# Set the legend's position
ax.legend(loc='upper left')

# Set the title and labels
ax.set_title('Government Policy Priorities by Category')
ax.set_xlabel('Category')
ax.set_ylabel('Percentage (%)')

# Automatically resize the image
fig.tight_layout()

# Save the image as output/final/area_chart/png/20231228-155112_16.png
fig.savefig('output/final/area_chart/png/20231228-155112_16.png', bbox_inches='tight')

# Clear the current image state
plt.clf()