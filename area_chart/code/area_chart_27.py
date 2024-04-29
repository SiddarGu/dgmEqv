
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data
data = {'Employee Type': ['HR', 'Managers', 'IT', 'Sales', 'Customer Service', 'Finance', 'Operations', 'Research & Development', 'Marketing', 'Legal', 'Administrative', 'Logistics', 'Communications'],
        'Full-time': [180, 200, 300, 250, 150, 180, 220, 250, 200, 150, 170, 180, 250],
        'Part-time': [120, 100, 150, 100, 50, 80, 120, 100, 80, 50, 70, 100, 80],
        'Contract': [50, 80, 70, 60, 20, 40, 50, 50, 30, 20, 40, 30, 40]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10, 8))

# Create axes
ax = fig.add_subplot(111)

# Define x and y ticks
x_ticks = np.arange(len(df.index))
y_ticks = np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, df.iloc[:, 1:].sum(axis=1).max())

# Set x and y ticks
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)

# Set x and y ticklabels
ax.set_xticklabels(df['Employee Type'])
ax.set_yticklabels(y_ticks)

# Set grid lines
ax.grid(True, alpha=0.3)

# Plot the data as an area chart
ax.stackplot(x_ticks, df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=['Full-time', 'Part-time', 'Contract'], colors=['#7EB5E6', '#8CC152', '#F6BB42'], alpha=0.8)

# Set legend
ax.legend(loc='upper right')

# Set title
ax.set_title('Employee Distribution by Department and Type')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231226-130527_11.png', bbox_inches='tight')

# Clear current image state
plt.clf()