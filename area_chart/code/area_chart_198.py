
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Convert data to dictionary
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Administration': [200, 180, 220, 210, 250],
    'Sales': [280, 300, 320, 310, 290],
    'IT': [270, 250, 230, 240, 260],
    'HR': [150, 160, 170, 180, 190],
    'R&D': [180, 200, 210, 190, 230]
}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figsize parameter to a larger setting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data as area chart
ax.stackplot(df['Year'], df['Administration'], df['Sales'], df['IT'], df['HR'], df['R&D'], labels=['Administration', 'Sales', 'IT', 'HR', 'R&D'])

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, df.iloc[:, 1:].sum(axis=1).max())

# Calculate max total value and ceil up to nearest multiple of 100
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 100) * 100

# Set yticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Number of Employees')

# Set title
ax.set_title('Employee Distribution by Department from 2018 to 2022')

# Set background grid lines
ax.grid(alpha=0.3)

# Set legend and its position
ax.legend(loc='upper left')

# Automatically resize image
plt.tight_layout()

# Save image with bbox_inches='tight'
plt.savefig('output/final/area_chart/png/20231228-145339_33.png', bbox_inches='tight')

# Clear current image state
plt.clf()