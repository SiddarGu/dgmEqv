

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import random

# Define data
data = {'Month': ['January', 'February', 'March', 'April', 'May'],
        'Raw Materials (ton)': [100, 90, 110, 120, 115],
        'Production Output (ton)': [80, 85, 90, 95, 100],
        'Waste (ton)': [10, 12, 15, 10, 13]}

# Process data
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and labels
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df['Month'])
ax.set_xlim(0, len(df.index) - 1)

# Calculate and set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Plot area chart
ax.stackplot(df.index, df['Raw Materials (ton)'], df['Production Output (ton)'], df['Waste (ton)'],
             labels=['Raw Materials (ton)', 'Production Output (ton)', 'Waste (ton)'],
             colors=['#85C2D9', '#FFB08E', '#FF7F7F'], alpha=0.7)

# Set legend
ax.legend(loc='upper right')

# Set title and labels
ax.set_title('Manufacturing Efficiency and Waste Reduction')
ax.set_xlabel('Month')
ax.set_ylabel('Amount (ton)')

# Automatically resize image and save
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231226-103019_5.png', bbox_inches='tight')

# Clear current image state
plt.clf()