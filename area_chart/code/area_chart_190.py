

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Represent the data using a dictionary
data = {'Year': [2018, 2019, 2020, 2021, 2022], 'Total Sales ($)': [100000, 120000, 140000, 160000, 180000], 'Marketing ($)': [20000, 25000, 28000, 30000, 32000], 'Operations ($)': [25000, 27000, 30000, 32000, 35000], 'Research & Development ($)': [30000, 28000, 29000, 31000, 33000], 'Infrastructure ($)': [25000, 32000, 33000, 36000, 39000]}

# Use pandas to process the data
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(15,10))

# Set the title
ax.set_title('Business Revenue and Expenditure from 2018 to 2022')

# Set the background grid lines
ax.grid(color='lightgrey', linestyle='--')

# Set the x and y axis ticks with a 70% probability
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0])

    # Set the rotation and rotation mode for the x-axis labels
    ax.tick_params(axis='x', rotation=45, ha='right', rotation_mode='anchor')

if np.random.choice([True, False], p=[0.7, 0.3]):
    # Calculate the max total value
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    # Round up to the nearest multiple of 10, 100, or 1000 depending on the specific value
    if max_total_value < 100:
        max_total_value = np.ceil(max_total_value / 10) * 10
    elif max_total_value < 1000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    # Set the y axis ticks and tick labels
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot the data using a stacked area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=df.columns[1:], alpha=0.8)

# Set the legend and adjust its position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-145339_21.png', bbox_inches='tight')

# Clear the current image state
plt.clf()