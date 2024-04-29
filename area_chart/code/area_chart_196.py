
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary and convert first column to string type
data = {'Mode of Transportation': ['Air', 'Rail', 'Road', 'Water', 'Pipeline'],
        'Number of Trips (Thousands)': [500, 600, 800, 300, 200],
        'Distance Traveled (Miles)': [10000, 20000, 50000, 15000, 1000]}
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value and round up to nearest multiple of 1000
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000

# Set x and y ticks with random length between 3 and 11
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_xlim(0, len(df.index) - 1)

# Plot area chart
ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.iloc[:, 0], colors=['#FFC000', '#0070C0', '#92D050', '#FF0000', '#7030A0'], alpha=0.75)

# Add gridlines randomly
ax.grid(axis='both', alpha=np.random.uniform(0.2, 0.5))

# Set legend and labels
ax.legend(loc='upper left', title='Mode of Transportation')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Trips (Thousands)', fontsize=12)

# Set title
ax.set_title('Transportation and Logistics Trends', fontsize=14)

# Automatically resize image and save
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-145339_30.png', bbox_inches='tight')

# Clear current image state
plt.clf()