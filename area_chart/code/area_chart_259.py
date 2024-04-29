
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data as dictionary
data = {'Category': ['IT', 'Marketing', 'Finance', 'Education', 'Healthcare', 'Science', 'Business', 'Government', 'E-commerce', 'Gaming', 'Mobile', 'Retail', 'Telecommunications', 'Automotive'],
        'Revenue ($)': [25000, 18000, 22000, 20000, 24000, 19000, 23000, 22000, 18000, 16000, 21000, 22000, 24000, 19000],
        'Expenses ($)': [19000, 15000, 20000, 18000, 21000, 17000, 19000, 20000, 16000, 15000, 18000, 21000, 22000, 18000],
        'Profit ($)': [6000, 3000, 2000, 2000, 3000, 2000, 4000, 2000, 2000, 1000, 3000, 1000, 2000, 1000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value and set y limit and ticks
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_ylim(0, max_total_value)
ax.set_yticks(yticks)

# Set background grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Plot data as stackplot
ax.stackplot(df.index, df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=['Revenue', 'Expenses', 'Profit'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)

# Set x axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(df.index)
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# Set legend and position
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# Set title and axis labels
ax.set_title('Business and Finance Overview')
ax.set_xlabel('Category')
ax.set_ylabel('Amount (in $)')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_18.png', bbox_inches='tight')

# Clear current image state
plt.clf()