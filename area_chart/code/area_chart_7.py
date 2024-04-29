

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Represent data using a dictionary
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Facebook (Users)': [50000, 48000, 55000, 60000],
    'Twitter (Users)': [45000, 48000, 50000, 55000],
    'Instagram (Users)': [70000, 65000, 60000, 70000],
    'LinkedIn (Users)': [60000, 55000, 65000, 60000]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot data as area chart
fig, ax = plt.subplots(figsize=(10, 5)) # Set larger figsize to prevent content from being cut off
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=['Facebook (Users)', 'Twitter (Users)', 'Instagram (Users)', 'LinkedIn (Users)'], colors=['#3b5998', '#1da1f2', '#c13584', '#0077b5']) # Set colors for each platform
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), ncol=1) # Adjust legend position
ax.set_title('User Growth on Social Media Platforms') # Set title
ax.set_xlabel('Month') # Set x label
ax.set_ylabel('Number of Users') # Set y label

# Set ticks and tick labels with 70% probability
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(0, len(df.index), 1)) # Set x ticks
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor', wrap=True) # Set x tick labels with rotation and wrap
    ax.set_xlim(0, len(df.index) - 1) # Set x limit
if np.random.choice([True, False], p=[0.7, 0.3]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max() # Calculate max total value
    max_total_value = np.ceil(max_total_value / 100) * 100 # Round up to nearest multiple of 100
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # Set y ticks with random length from list
    ax.set_ylim(0, max_total_value) # Set y limit

# Set background grid lines
ax.grid(axis='both', linestyle=':', alpha=0.5)

# Automatically resize image before saving
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231226-103019_15.png', bbox_inches='tight')

# Clear current image state
plt.clf()