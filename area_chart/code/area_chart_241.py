

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {'Category':['Air','Road','Rail','Sea','Pipeline'],
        'Transportation (Units)':[200,300,150,100,250],
        'Logistics (Units)':[100,200,250,300,150],
        'Parcel Delivery (Units)':[300,150,100,200,250],
        'Freight Shipping (Units)':[150,100,200,250,300]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12,8))

# Set colors and transparency
colors = ['#3EB4C8', '#C74E3E', '#8DBE4E', '#C5C8C3']
alpha = 0.8

# Plot data with area chart
ax.stackplot(df['Category'], df['Transportation (Units)'], df['Logistics (Units)'], df['Parcel Delivery (Units)'], df['Freight Shipping (Units)'], labels=['Transportation (Units)', 'Logistics (Units)', 'Parcel Delivery (Units)', 'Freight Shipping (Units)'], colors=colors, alpha=alpha)

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(alpha=0.3)

# Set legend and position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title
ax.set_title('Transportation and Logistics Units by Mode of Transport')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_88.png', bbox_inches='tight')

# Clear current image state
plt.clf()