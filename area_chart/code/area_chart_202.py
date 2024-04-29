
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary for data
data = {'Category': ['Beverages (Revenue)', 'Snacks (Revenue)', 'Meals (Revenue)', 'Alcohol (Revenue)', 'Desserts (Revenue)', 'Fast Food (Revenue)', 'Groceries (Revenue)'],
        '2017': [500000, 300000, 250000, 150000, 200000, 400000, 600000],
        '2018': [550000, 320000, 280000, 180000, 220000, 450000, 650000],
        '2019': [600000, 350000, 300000, 200000, 250000, 500000, 700000],
        '2020': [650000, 380000, 320000, 220000, 280000, 550000, 750000],
        '2021': [700000, 400000, 350000, 250000, 300000, 600000, 800000]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Plot area chart
ax = plt.subplot()
ax.stackplot(df['Category'], df['2017'], df['2018'], df['2019'], df['2020'], df['2021'], labels=['2017', '2018', '2019', '2020', '2021'])

# Set x and y axis ticks and ticklabels
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set y limit
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
plt.ylim(0, np.ceil(max_total_value / 1000) * 1000)

# Set grid lines
plt.grid(axis='y')

# Set legend
plt.legend(loc='upper left')

# Set title
plt.title('Revenue Distribution in the Food and Beverage Industry from 2017 to 2021')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-145339_37.png', bbox_inches='tight')

# Clear current image state
plt.clf()