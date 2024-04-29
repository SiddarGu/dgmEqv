


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as dictionary
data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Public Transportation Budget ($)': [5000, 5200, 4500, 5100, 4800],
        'Infrastructure Development Budget ($)': [4000, 4100, 4900, 3500, 3900],
        'Education Budget ($)': [6000, 5500, 3300, 3200, 2800],
        'Health Care Budget ($)': [3000, 2200, 2800, 2500, 2900],
        'Defense Budget ($)': [2000, 1950, 2100, 2200, 2300]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with area chart
fig, ax = plt.subplots(figsize=(12,8), dpi=100)
ax.stackplot(df['Year'], df['Public Transportation Budget ($)'], df['Infrastructure Development Budget ($)'], df['Education Budget ($)'], df['Health Care Budget ($)'], df['Defense Budget ($)'], labels=['Public Transportation', 'Infrastructure Development', 'Education', 'Health Care', 'Defense'], colors=['#ff8c00', '#87ceeb', '#ffd700', '#ff69b4', '#daa520'], alpha=0.7)

# Set x and y axis ticks and ticklabels randomly
if np.random.randint(0, 10) < 7:
    ax.set_xlim(0, len(df.index) - 1)
    xticks = np.arange(0, len(df.index), 1)
    ax.set_xticks(xticks)
    ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value < 100:
        yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
        ax.set_yticks(yticks)
        ax.set_yticklabels(yticks, rotation=0, ha='right', rotation_mode='anchor')
    elif max_total_value < 1000:
        max_total_value = np.ceil(max_total_value/100)*100
        yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
        ax.set_yticks(yticks)
        ax.set_yticklabels(yticks, rotation=0, ha='right', rotation_mode='anchor')
    else:
        max_total_value = np.ceil(max_total_value/1000)*1000
        yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
        ax.set_yticks(yticks)
        ax.set_yticklabels(yticks, rotation=0, ha='right', rotation_mode='anchor')
else:
    ax.set_xticks([])
    ax.set_yticks([])

# Set background grid lines randomly
if np.random.randint(0, 10) < 7:
    ax.grid(linestyle='-', color='grey', alpha=0.3)

# Set legend position
ax.legend(loc='upper left')

# Automatically resize image
fig.tight_layout()

# Set title
ax.set_title('Government Budget Allocation by Year', fontsize=16)

# Save figure
fig.savefig('output/final/area_chart/png/20231228-145339_32.png', bbox_inches='tight')

# Clear current image state
plt.clf()