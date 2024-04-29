
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Convert data to dictionary
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Electricity (MWh)': [200000, 180000, 190000, 220000, 210000, 240000, 230000, 220000, 210000, 240000, 230000, 220000],
        'Natural Gas (MMBTU)': [100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000, 210000],
        'Water (Million Gallons)': [50000, 55000, 60000, 50000, 45000, 40000, 35000, 30000, 25000, 20000, 15000, 10000],
        'Renewable Energy (MWh)': [50000, 40000, 45000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with the type of area chart
fig, ax = plt.subplots(figsize=(10,6))
ax.stackplot(df['Month'], df['Electricity (MWh)'], df['Natural Gas (MMBTU)'], df['Water (Million Gallons)'], df['Renewable Energy (MWh)'], labels=['Electricity (MWh)', 'Natural Gas (MMBTU)', 'Water (Million Gallons)', 'Renewable Energy (MWh)'], colors=['#FFB6C1', '#87CEEB', '#FFDAB9', '#90EE90'], alpha=0.8)

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000 # Round up to nearest multiple of 1000
ax.set_ylim(0, max_total_value)
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set background grid lines
plt.grid(linestyle='--')

# Set legend and labels
ax.legend(loc='upper left')
ax.set_xlabel('Month')
ax.set_ylabel('Usage')
ax.set_title('Energy and Utilities Usage by Month', fontsize=12)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-131755_67.png', bbox_inches='tight')

# Clear the current image state
plt.clf()