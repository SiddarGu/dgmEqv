
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {'City': ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia'],
        'Average House Price (Millions)': [2.5, 1.8, 1.2, 1.0, 0.9, 1.1],
        'Median House Price (Millions)': [2.0, 1.6, 1.0, 0.9, 0.8, 0.9],
        'Average Rent (Thousands)': [3.8, 2.5, 1.8, 1.3, 1.2, 1.5],
        'Vacancy Rate (%)': [5, 7, 10, 12, 8, 9],
        'Foreclosure Rate (%)': [2, 1.5, 3, 2.5, 2, 3]}

# Create a dataframe from data
df = pd.DataFrame(data)

# Set style for seaborn heatmap
sns.set(style="white")

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Create heatmap using seaborn
sns.heatmap(df.iloc[:, 1:], annot=True, cmap='Blues', fmt='.1f', linewidths=.5, cbar_kws={'label': 'Percentage'})

# Set title and x/y axis labels
plt.title('Housing Market Analysis by City')
plt.xlabel('Property Type')
plt.ylabel('City')

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(5) + .5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticks(np.arange(6) + .5)
ax.set_yticklabels(df['City'], rotation=0, ha='right', rotation_mode='anchor', wrap=True)

# Center x and y ticks
ax.tick_params(axis='x', which='major', pad=10)
ax.tick_params(axis='y', which='major', pad=10)

# Automatically resize image by tight_layout()
fig.tight_layout()

# Save figure in relative path
plt.savefig('output/final/heatmap/png/20231228-131639_89.png', bbox_inches='tight')

# Clear current image state
plt.clf()
plt.close()

# Print success message
print("The chart has been successfully saved in output/final/heatmap/png/20231228-131639_89.png")