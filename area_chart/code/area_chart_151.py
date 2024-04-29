
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {
    'Year': [2016, 2017, 2018, 2019, 2020],
    'Electricity Investment ($)': [20000, 18000, 25000, 22000, 24000],
    'Gas Investment ($)': [15000, 12000, 13000, 14000, 16000],
    'Oil Investment ($)': [18000, 20000, 15000, 17000, 13000],
    'Coal Investment ($)': [13000, 17000, 16000, 19000, 15000],
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10, 8))

# Plot the chart
ax = fig.add_subplot(111)
ax.stackplot(df['Year'], df['Electricity Investment ($)'], df['Gas Investment ($)'], df['Oil Investment ($)'], df['Coal Investment ($)'], labels=['Electricity', 'Gas', 'Oil', 'Coal'], colors=['#FFD700', '#FFA500', '#FF0000', '#000000'], alpha=0.6)

# Set ticks and ticklabels for x-axis
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(0, len(df.index), 1))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# Set ticks and ticklabels for y-axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10000) * 10000 # Round up to nearest multiple of 10000
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, rotation=0, ha='right', rotation_mode='anchor')

# Set background grid lines
ax.grid(color='#D3D3D3', linestyle=':', linewidth=0.5)

# Set legend and legend position
handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper left')

# Set title
ax.set_title('Energy and Utilities Investment Trends')

# Automatically resize image and save
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-140159_68.png', bbox_inches='tight')

# Clear current image state
plt.clf()