
# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create dictionary for data
data = {'2017': ['Q1', 'Q2', 'Q3', 'Q4'],
        'Primary Care Visits': [200, 100, 150, 100],
        'Specialty Care Visits': [150, 120, 180, 200],
        'Emergency Visits': [180, 150, 200, 250],
        'Inpatient Visits': [130, 100, 150, 180],
        'Outpatient Visits': [250, 200, 250, 150]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Primary Care Visits', 'Specialty Care Visits', 'Emergency Visits', 'Inpatient Visits', 'Outpatient Visits'], colors=['#6bb9f0', '#ff9e3c', '#ff6e83', '#b3b3b3', '#6a6a6a'], alpha=0.8)

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10)*10
ax.set_ylim(0, max_total_value)

# Set ticks and tick labels for x and y axis
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(ls=':', alpha=0.5)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title
ax.set_title('Healthcare Visits by Type and Quarter in 2017')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-140159_95.png', bbox_inches='tight')

# Clear current image state
plt.clf()
