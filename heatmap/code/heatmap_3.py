
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the data
data = {'Category': ['Education', 'Healthcare', 'Infrastructure', 'Environment', 'Finance'], 
        'Number of Laws Passed': [50, 40, 25, 35, 30], 
        'Number of Regulations Issued': [150, 100, 75, 120, 80], 
        'Amount of Government Spending (Billion USD)': [100, 200, 150, 75, 175], 
        'Percentage of Population Affected (%)': [25, 30, 20, 10, 15], 
        'Number of Government Programs': [10, 15, 5, 8, 12]}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Set the index as the Category column
df.set_index('Category', inplace=True)

# Set the figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the heatmap using the seaborn library
sns.heatmap(df, annot=True, cmap='Blues', fmt='g', linewidths=.5, cbar=False)

# Set the x and y ticks and tick labels
ax.set_xticklabels(df.columns, rotation=45, ha='right')
ax.set_yticklabels(df.index, rotation=0, ha='center')

# Set the title
ax.set_title('Government Policy Metrics')

# Automatically resize the image and save it
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231225-210514_17.png', bbox_inches='tight')

# Clear the current image state
plt.clf()