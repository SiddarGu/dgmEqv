
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Represent data using a dictionary
data = {'Year': [2017, 2018, 2019, 2020, 2021],
        'Performing Arts (%)': [25, 20, 30, 15, 20],
        'Visual Arts (%)': [20, 25, 15, 20, 15],
        'Literature (%)': [10, 15, 20, 25, 10],
        'Film (%)': [15, 10, 10, 10, 25],
        'Music (%)': [30, 30, 25, 30, 30]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create ax
fig, ax = plt.subplots(figsize=(10, 6))

# Plot area chart
ax.stackplot(df['Year'], df['Performing Arts (%)'], df['Visual Arts (%)'], df['Literature (%)'], df['Film (%)'], df['Music (%)'],
             labels=['Performing Arts', 'Visual Arts', 'Literature', 'Film', 'Music'], alpha=0.8)

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set tick labels with rotation and wrapping
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(yticks, wrap=True)

# Set grid lines
ax.grid(color='lightgrey', linestyle='--', linewidth=0.5)

# Set legend and title
ax.legend(loc='upper left')
ax.set_title('Trends in Arts and Culture Participation by Year')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_0.png', bbox_inches='tight')

# Clear current image state
plt.clf()