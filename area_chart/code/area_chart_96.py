
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Convert data to dictionary
data_dict = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Revenue ($)': [50000, 60000, 55000, 70000, 55000, 65000, 60000, 50000, 55000, 60000, 65000, 70000],
    'Expenses ($)': [45000, 50000, 46000, 60000, 48000, 55000, 49000, 45000, 50000, 55000, 60000, 65000],
    'Profit ($)': [5000, 10000, 9000, 10000, 7000, 10000, 11000, 5000, 5000, 5000, 5000, 5000]
}

# Process data using pandas
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(12, 8))

# Plot the data with area chart
ax = plt.gca()
ax.stackplot(df['Month'], df['Revenue ($)'], df['Expenses ($)'], df['Profit ($)'], labels=['Revenue', 'Expenses', 'Profit'], colors=['#5ca8d1', '#f0a1a1', '#c7c7c7'], alpha=0.7)

# Set background grid lines
plt.grid(color='#d9d9d9', linestyle='-', linewidth=0.5)

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 100:
    max_total_value = max_total_value + 10
elif max_total_value > 100 and max_total_value < 1000:
    max_total_value = np.ceil(max_total_value/10)*10
elif max_total_value > 1000 and max_total_value < 10000:
    max_total_value = np.ceil(max_total_value/100)*100
else:
    max_total_value = np.ceil(max_total_value/1000)*1000
ax.set_ylim(0, max_total_value)

# Set y ticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set tick labels
ax.set_xticklabels(df['Month'], rotation=45, ha='right', rotation_mode='anchor')

# Set legend position
plt.legend(loc='upper right')

# Set title
plt.title('Business Revenue and Expenses in 2020')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-131755_82.png', bbox_inches='tight')

# Clear current image state
plt.clf()