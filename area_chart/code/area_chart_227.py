
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as dictionary
data = {
    'Year': [2017, 2018, 2019, 2020, 2021],
    'Music (Events)': [200, 250, 180, 150, 130],
    'Theatre (Events)': [150, 200, 130, 180, 200],
    'Museum (Events)': [180, 150, 200, 130, 150],
    'Art Exhibition (Events)': [130, 180, 150, 200, 180]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10, 8))

# Set background grid lines
plt.grid(linestyle='dashed', color='grey', alpha=0.5)

# Plot the data with stackplot
ax = plt.subplot()
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=['Music (Events)', 'Theatre (Events)', 'Museum (Events)', 'Art Exhibition (Events)'], colors=['#FF6B6B', '#FFD166', '#6AB04C', '#4A4E69'], alpha=0.8)

# Set x and y axis ticks and ticklabels with 70% probability
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(5))
    ax.set_xticklabels(df.iloc[:, 0])

    # Rotate x-axis labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

if np.random.choice([True, False], p=[0.7, 0.3]):
    # Calculate max total value
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()

    # Round up max total value to nearest multiple of 10, 100, or 1000
    if max_total_value < 100:
        max_total_value = np.ceil(max_total_value / 10) * 10
    elif max_total_value < 1000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000

    # Set y axis limit and ticks
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend and position
plt.legend(loc='upper right')

# Set title
plt.title('Events by Category from 2017 to 2021')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_71.png', bbox_inches='tight')

# Clear current image state
plt.clf()