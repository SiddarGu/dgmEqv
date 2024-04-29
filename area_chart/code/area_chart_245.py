
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data as a dictionary
data = {'Category': ['Art Galleries', 'Concerts', 'Museums', 'Theater', 'Festivals'],
        '2021': [250, 180, 200, 150, 280],
        '2022': [280, 200, 220, 180, 300],
        '2023': [300, 220, 250, 200, 320],
        '2024': [320, 250, 280, 220, 350]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10

# Set x and y axis tick labels and ticks
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set colors and transparency
colors = ['#FFB6C1', '#87CEEB', '#98FB98', '#FFA07A', '#FFDAB9']
alpha = 0.7

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=alpha)

# Set legend position and title
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.title('Visitor Trends in Arts and Culture Events from 2021 to 2024')

# Set background grid lines
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_92.png', bbox_inches='tight')

# Clear image state
plt.clf()