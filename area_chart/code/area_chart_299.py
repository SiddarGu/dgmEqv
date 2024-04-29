
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create data dictionary
data = {'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'], 'Revenue ($)': [50000, 52000, 45000, 51000], 'Expenses ($)': [40000, 41000, 49000, 35000], 'Profit ($)': [10000, 11000, 14000, 16000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create axes object
fig, ax = plt.subplots(figsize=(12, 8))

# Plot area chart
ax.stackplot(df['Quarter'], df['Revenue ($)'], df['Expenses ($)'], df['Profit ($)'], labels=['Revenue', 'Expenses', 'Profit'], colors=['#3CAEA3', '#F6D55C', '#ED553B'], alpha=0.7)

# Adjust legend position
ax.legend(loc='upper left')

# Set x and y axis ticks and labels
ax.set_xticks(np.arange(len(df['Quarter'])))
ax.set_xticklabels(df['Quarter'])
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and set suitable y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 100:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
elif max_total_value <= 1000:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
elif max_total_value <= 10000:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
else:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set background grid lines
ax.grid(axis='y', linestyle='--')

# Set title and labels
ax.set_title('Quarterly Financial Performance')
ax.set_xlabel('Quarter')
ax.set_ylabel('Amount ($)')
ax.set_yticklabels(yticks)

# Automatically resize image
fig.tight_layout()
# Save figure
fig.savefig('output/final/area_chart/png/20231228-161902_8.png', bbox_inches='tight')

# Clear current image state
plt.cla()
plt.clf()
plt.close()