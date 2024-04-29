
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Year': ['2019', '2020', '2021', '2022', '2023'],
        'Mobile Users (millions)': [400, 450, 500, 550, 600],
        'Internet Users (millions)': [300, 350, 400, 450, 500],
        'Smartphone Users (millions)': [250, 300, 350, 400, 450],
        'Social Media Users (millions)': [200, 250, 300, 350, 400],
        'E-commerce Users (millions)': [150, 200, 250, 300, 350]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data as an area chart
ax.stackplot(df['Year'], df['Mobile Users (millions)'], df['Internet Users (millions)'], df['Smartphone Users (millions)'], df['Social Media Users (millions)'], df['E-commerce Users (millions)'], labels=['Mobile Users', 'Internet Users', 'Smartphone Users', 'Social Media Users', 'E-commerce Users'], colors=['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99'], alpha=0.7)

# Set ticks and ticklabels for x axis
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')

# Set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/100) * 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set legend position and title
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_title('Technology and Internet Usage Statistics from 2019 to 2023')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-103019_25.png', bbox_inches='tight')

# Clear the current image state
plt.clf()