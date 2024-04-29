

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Legislation Passed (%)': [80, 75, 70, 65, 60],
        'Policy Changes (%)': [70, 65, 60, 55, 50],
        'Budget Allocation (%)': [60, 55, 50, 45, 40],
        'Public Opinion (%)': [50, 45, 40, 35, 30]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data with stackplot
ax.stackplot(df['Year'], df['Legislation Passed (%)'], df['Policy Changes (%)'], df['Budget Allocation (%)'], df['Public Opinion (%)'], labels=['Legislation Passed', 'Policy Changes', 'Budget Allocation', 'Public Opinion'], colors=['#0096FF', '#00B1B1', '#4374B3', '#6FA8DC'], alpha=0.7)

# Set x and y axis ticks and ticklabels
if np.random.rand() < 0.7:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Year'])
    ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(ax.get_yticks(), rotation=45, ha='right', rotation_mode='anchor')

# Set background grid lines
ax.grid(linestyle='dotted', linewidth=0.5)

# Set legend and legend's position
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4)

# Set title
ax.set_title('Government and Public Policy Trends')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-145339_35.png', bbox_inches='tight')

# Clear the current image state
plt.clf()