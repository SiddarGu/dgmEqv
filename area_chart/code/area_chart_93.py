
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {'Year': ['2019', '2020', '2021', '2022', '2023'],
        'Administration (Employees)': [200, 180, 220, 210, 250],
        'Sales (Employees)': [280, 300, 320, 310, 290],
        'IT (Employees)': [270, 250, 230, 240, 260],
        'HR (Employees)': [150, 160, 170, 180, 190],
        'R&D (Employees)': [180, 200, 210, 190, 230]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figsize parameter
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data with area chart
ax.stackplot(df['Year'], df.iloc[:, 1:].T, labels=df.columns[1:], colors=['#FFA07A', '#87CEEB', '#90EE90', '#FFDAB9', '#B0C4DE'], alpha=0.7)

# Set ticks and ticklabels for x and y axis
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(0, len(df.index), 1))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# Calculate max total value and set yticks
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 100) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.5)

# Set legend and adjust its position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title and ylabels
ax.set_title('Employee Distribution by Department from 2019 to 2023')
ax.set_ylabel('Number of Employees')

# Automatically resize image and save it
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_78.png', bbox_inches='tight')

# Clear current image state
plt.clf()