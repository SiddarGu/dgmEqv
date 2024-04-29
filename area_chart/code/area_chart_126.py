


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define and process data
data = {'Category': ['California', 'Texas', 'New York', 'Florida', 'Illinois', 'Pennsylvania', 'Ohio', 'Arizona', 'Michigan', 'North Carolina', 'Georgia'],
        'Luxury Homes (Sales)': [200, 150, 180, 250, 120, 200, 160, 140, 180, 150, 200],
        'Single Family Homes (Sales)': [300, 250, 200, 150, 180, 160, 180, 190, 150, 180, 170],
        'Condos (Sales)': [150, 180, 130, 120, 200, 140, 150, 180, 200, 160, 150],
        'Townhomes (Sales)': [120, 100, 150, 200, 130, 180, 220, 160, 170, 190, 240],
        'Rentals (Leases)': [220, 260, 240, 270, 190, 210, 200, 170, 190, 230, 210]}
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5],
              labels=['Luxury Homes (Sales)', 'Single Family Homes (Sales)', 'Condos (Sales)', 'Townhomes (Sales)', 'Rentals (Leases)'],
              colors=['#0096FF', '#8EE5EE', '#FFB6C1', '#FFA500', '#90EE90'], alpha=0.8)

# Set x and y axis ticks and ticklabels
if np.random.choice([0, 1], p=[0.3, 0.7]):
    ax.set_xticks(np.arange(0, len(df.index), 1))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
    ax.set_xlim(0, len(df.index) - 1)
if np.random.choice([0, 1], p=[0.3, 0.7]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
if np.random.choice([0, 1], p=[0.3, 0.7]):
    ax.grid(linestyle='dashed', alpha=0.5)

# Set legend and legend title
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5, frameon=False)
legend_title = ax.set_title('Legend', fontsize=12)
legend_title.set_y(1.15)

# Set y axis label
if np.random.choice([0, 1], p=[0.3, 0.7]):
    ax.set_ylabel('Number of Sales', fontsize=12)

# Set title
ax.set_title('Real Estate and Housing Market Trends by Region', fontsize=14)

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_39.png', bbox_inches='tight')

# Clear image state
plt.clf()
plt.close()