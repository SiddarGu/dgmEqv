
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data
data = {'Year': ['2019', '2020', '2021', '2022', '2023'],
        'Administration (Employees)': [200, 180, 220, 210, 250],
        'Sales (Employees)': [280, 300, 320, 310, 290],
        'IT (Employees)': [270, 250, 230, 240, 260],
        'HR (Employees)': [150, 160, 170, 180, 190],
        'R&D (Employees)': [180, 200, 210, 190, 230]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10,8))

# Plot the data with area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Administration', 'Sales', 'IT', 'HR', 'R&D'], colors=['#e74c3c', '#3498db', '#2ecc71', '#f1c40f', '#9b59b6'], alpha=0.8)

# Set axis limits and ticks
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)
ax.set_xticks(np.linspace(0, len(df.index) - 1, 5, dtype=np.int32))
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Number of Employees')

# Set title
ax.set_title('Employee Distribution by Department from 2019 to 2023')

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--', linewidth=0.5, alpha=0.5)

# Set legend
ax.legend(loc='upper left')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-155112_59.png', bbox_inches='tight')

# Clear figure
plt.clf()