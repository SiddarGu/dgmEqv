
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary and convert first column to string type
data = {'Year': ['2016', '2017', '2018', '2019', '2020', '2021', '2022'],
        'Single Family Homes (Units)': [400, 500, 600, 700, 800, 900, 1000],
        'Condominiums (Units)': [300, 350, 400, 450, 500, 550, 600],
        'Townhomes (Units)': [200, 250, 300, 350, 400, 450, 500],
        'Apartments (Units)': [100, 150, 200, 250, 300, 350, 400]}
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and probability of setting ticks and ticklabels
fig, ax = plt.subplots(figsize=(12,8))
prob = 0.7

# Calculate max total value and set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_ylim(0, max_total_value)
ax.set_yticks(yticks)

# Set x axis range
ax.set_xlim(0, len(df.index) - 1)

# Plot area chart for each unit type
ax.stackplot(df['Year'], df['Single Family Homes (Units)'], df['Condominiums (Units)'], df['Townhomes (Units)'], df['Apartments (Units)'], labels=['Single Family Homes', 'Condominiums', 'Townhomes', 'Apartments'], colors=['#6c8cd5', '#ff7f50', '#ba55d3', '#ffa500'], alpha=0.7)

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set legend and legend position
ax.legend(loc='upper left')
plt.legend(frameon=False)

# Set ticks and ticklabels for x axis
if np.random.choice([True, False], p=[prob, 1-prob]):
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')
else:
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Year'], wrap=True)

# Set title and labels
plt.title('Housing Market Trends by Unit Type from 2016 to 2022')
plt.xlabel('Year')
plt.ylabel('Units')

# Automatically resize and save image
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_70.png', bbox_inches='tight')

# Clear image state
plt.close()