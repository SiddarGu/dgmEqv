
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

# Define data dictionary
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Electricity (kWh)': [25000, 26000, 27000, 28000, 29000],
        'Water (gallons)': [5000, 5100, 5200, 5300, 5400],
        'Gas (m3)': [2000, 2100, 2200, 2300, 2400]}

# Create pandas dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value and round up to nearest multiple of 100
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100

# Set y limits and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x limits and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])

# Set x and y axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Usage')

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3],
             labels=['Electricity', 'Water', 'Gas'], colors=['#0066CC', '#00CC66', '#FF9900'], alpha=0.8)

# Show grid lines
ax.grid(color='gray', linestyle='--')

# Set legend
ax.legend(loc='upper left')

# Set title
plt.title('Energy and Utilities Usage by Year')

# Automatically resize image
fig.tight_layout()

# Save figure as png
plt.savefig('output/final/area_chart/png/20231228-131755_80.png', bbox_inches='tight')

# Clear figure
plt.clf()