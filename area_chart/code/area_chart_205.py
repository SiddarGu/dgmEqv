
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Year': ['2019', '2020', '2021', '2022', '2023'],
        'Recruitment (Employees)': [200, 250, 180, 150, 200],
        'Training (Employees)': [150, 180, 200, 180, 180],
        'Compensation (Employees)': [180, 200, 150, 130, 150],
        'Benefits (Employees)': [130, 150, 100, 200, 130],
        'Performance Management (Employees)': [250, 250, 250, 170, 100]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value and round up to nearest multiple of 10, 100, or 1000
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value > 1000:
    max_total_value = np.ceil(max_total_value / 1000) * 1000
elif max_total_value > 100:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 10) * 10

# Set y ticks and tick labels
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
yticklabels = ['${:,.0f}'.format(x) for x in yticks]
ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)

# Set x ticks and tick labels
ax.set_xticks(np.arange(len(df)))
ax.set_xticklabels(df['Year'])

# Plot area chart
ax.stackplot(df['Year'], df.iloc[:, 1:].transpose(), labels=df.iloc[:, 1:].columns, colors=['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3'], alpha=0.8)

# Set legend and position
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)

# Set title
ax.set_title('Employee Distribution by HR Functions from 2019 to 2023')

# Set grid lines
ax.grid(linestyle='--', alpha=0.5)

# Automatically resize image
plt.tight_layout()

# Save figure as png
plt.savefig('output/final/area_chart/png/20231228-145339_40.png', bbox_inches='tight')

# Clear figure
plt.clf()