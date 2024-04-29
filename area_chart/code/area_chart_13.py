
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data
data = {'Month': ['January', 'February', 'March', 'April', 'May'], 'Revenue ($)': [500000, 480000, 520000, 450000, 540000], 'Expenses ($)': [450000, 430000, 460000, 400000, 490000], 'Profit ($)': [50000, 50000, 60000, 50000, 50000]}

# Process data into dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=['Revenue', 'Expenses', 'Profit'], colors=['#FFB4B4', '#B4D8FF', '#B4FFB4'], alpha=0.7)

# Set x and y axis tick labels and rotation
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000)

# Set grid lines
ax.grid(color='gray', linestyle='--')

# Add legend and set its position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title and labels
ax.set_title('Monthly Retail and E-commerce Performance')
ax.set_xlabel('Month')
ax.set_ylabel('Amount ($)')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-103019_22.png', bbox_inches='tight')

# Clear current image state
plt.clf()