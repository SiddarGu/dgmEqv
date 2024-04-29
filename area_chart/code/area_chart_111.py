
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary with the given data
data = {
    'Year': ['2019', '2020', '2021', '2022', '2023'],
    'Educational Budget ($)': [10000, 11000, 12000, 13000, 14000],
    'Healthcare Budget ($)': [12000, 13000, 14000, 15000, 16000],
    'Infrastructure Budget ($)': [8000, 9000, 10000, 11000, 12000],
    'Defense Budget ($)': [15000, 16000, 17000, 18000, 19000]
}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create a new figure and set the figure size
fig = plt.figure(figsize=(12,8))

# Get the maximum total value for y-axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Ceil the maximum total value up to the nearest multiple of 1000
max_total_value = int(np.ceil(max_total_value / 1000.0)) * 1000

# Set y-axis limit and ticks
plt.ylim(0, max_total_value)
plt.yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot the data as an area chart using ax.stackplot()
ax = plt.subplot()
ax.stackplot(df['Year'], df['Educational Budget ($)'], df['Healthcare Budget ($)'], df['Infrastructure Budget ($)'], df['Defense Budget ($)'], labels=['Educational Budget', 'Healthcare Budget', 'Infrastructure Budget', 'Defense Budget'], colors=['#FFB6C1', '#1E90FF', '#FFDAB9', '#2E8B57'], alpha=0.7)

# Set x-axis limit and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df)))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')

# Add grid lines
ax.grid(axis='y')

# Set legend position and add title
ax.legend(loc='upper left')
plt.title('Government Budget Allocation from 2019 to 2023')

# Automatically resize the image before saving
plt.tight_layout()

# Save the figure as a png file
fig.savefig('output/final/area_chart/png/20231228-140159_19.png', bbox_inches='tight')

# Clear the current image state
plt.clf()