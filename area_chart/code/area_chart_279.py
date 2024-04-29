
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Category': ['North America', 'Europe', 'Asia', 'South America', 'Africa'],
        'Football (Fans)': [30000, 25000, 15000, 20000, 10000],
        'Basketball (Fans)': [25000, 30000, 10000, 15000, 20000],
        'Baseball (Fans)': [20000, 15000, 20000, 25000, 30000],
        'Soccer (Fans)': [15000, 20000, 25000, 10000, 25000],
        'Tennis (Fans)': [10000, 10000, 30000, 30000, 15000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10,6))

# Set background grid lines
ax.grid()

# Plot data as stacked area chart
ax.stackplot(df['Category'], df.iloc[:, 1:].T, labels=df.columns[1:])

# Set x and y axis labels
ax.set_xlabel('Region')
ax.set_ylabel('Number of Fans')

# Set title
ax.set_title('Fan Distribution by Region for Popular Sports')

# Set legend
ax.legend(loc='upper right')

# Set ticks and tick labels for x axis
ax.set_xticks(np.arange(len(df['Category'])))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Calculate max total value and set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/100) * 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-155112_43.png', bbox_inches='tight')

# Clear current image state
plt.clf()