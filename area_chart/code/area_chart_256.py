


# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data dictionary
data = {'Country': ['China', 'United States', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Italy', 'Brazil', 'Canada', 'Australia'], 
        'Production (Tonnes)': [200000, 150000, 120000, 100000, 80000, 60000, 50000, 40000, 30000, 20000, 10000],
        'Exports (Tonnes)': [150000, 120000, 80000, 90000, 60000, 50000, 45000, 35000, 25000, 18000, 8000],
        'Imports (Tonnes)': [100000, 90000, 60000, 80000, 50000, 40000, 30000, 20000, 15000, 10000, 6000]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Create axis object
ax = fig.add_subplot(111)

# Plot area chart
ax.stackplot(df.index, df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)

# Set x ticks and labels
ax.set_xticks(df.index)
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# Set y ticks and labels
max_total_val = df.iloc[:, 1:].sum(axis=1).max()
if max_total_val < 100:
    step = 10
elif max_total_val < 1000:
    step = 100
else:
    step = 1000
max_y_lim = np.ceil(max_total_val/step)*step
yticks = np.linspace(0, max_y_lim, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)

# Set grid lines
ax.grid(axis='both', alpha=0.3)

# Set legend
ax.legend(loc='lower right')

# Set title
ax.set_title('Manufacturing and Production Overview')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-155112_14.png', bbox_inches='tight')

# Clear current image state
plt.clf()