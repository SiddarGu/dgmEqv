


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data as dictionary
data = {'Category': ['North America', 'Europe', 'Asia', 'Africa', 'South America'],
        'Meat Production (lbs)': [100000, 90000, 110000, 80000, 100000],
        'Fish Production (lbs)': [80000, 70000, 90000, 60000, 80000],
        'Vegetable Production (lbs)': [120000, 110000, 130000, 100000, 120000],
        'Fruit Production (lbs)': [90000, 80000, 100000, 70000, 90000],
        'Dairy Production (lbs)': [150000, 140000, 160000, 130000, 150000]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10, 6))

# Plot the data as an area chart
ax = fig.add_subplot()
ax.stackplot(df['Category'], df.iloc[:, 1:6].values.T, labels=df.columns[1:6], alpha=0.8)

# Set x and y axis ticks and ticklabels
if np.random.rand() < 0.7:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(range(len(df.index)))
    ax.set_xticklabels(df['Category'])

# Calculate max total value and set yticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value >= 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
elif max_total_value >= 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
else:
    max_total_value = np.ceil(max_total_value)
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(color='lightgrey', linestyle='dashed')

# Add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# Set title
plt.title('Agricultural Production by Region')

# Automatically resize the image
plt.tight_layout()

# Save the chart
plt.savefig('output/final/area_chart/png/20231228-140159_52.png', bbox_inches='tight')

# Clear the current image state
plt.clf()