
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data = {'Category': ['Clothing', 'Electronics', 'Beauty & Personal Care', 'Home & Kitchen', 'Grocery', 'Toys & Games'], '2016 Sales': [100000, 500000, 80000, 150000, 400000, 100000], '2017 Sales': [110000, 560000, 90000, 160000, 420000, 110000], '2018 Sales': [120000, 600000, 100000, 170000, 440000, 120000], '2019 Sales': [130000, 620000, 110000, 180000, 460000, 130000], '2020 Sales': [140000, 650000, 120000, 190000, 480000, 140000]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figsize parameter
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data with type of area chart
ax.stackplot(df['Category'], df['2016 Sales'], df['2017 Sales'], df['2018 Sales'], df['2019 Sales'], df['2020 Sales'], labels=['2016 Sales', '2017 Sales', '2018 Sales', '2019 Sales', '2020 Sales'])

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set ticks and ticklabels for x axis
ax.set_xticks(range(len(df.index)))
ax.set_xticklabels(df['Category'])

# Set rotation for x axis
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Set ticks and ticklabels for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100 # Round up to nearest multiple of 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set rotation for y axis
plt.yticks(rotation=0)

# Set title
ax.set_title('Sales Trend for Retail and E-commerce Categories from 2016 to 2020')

# Set legend
ax.legend(loc='upper left')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-131755_17.png', bbox_inches='tight')

# Clear current image state
plt.clf()