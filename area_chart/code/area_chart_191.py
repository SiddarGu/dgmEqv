
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as dictionary
data = {'Sector': ['Agriculture', 'Manufacturing', 'Real Estate', 'Technology', 'Healthcare', 'Retail', 'Finance', 'Transportation', 'Energy', 'Media', 'Construction', 'Tourism'], 'Investment ($)': [50000, 80000, 70000, 100000, 90000, 60000, 110000, 80000, 90000, 70000, 50000, 60000], 'Revenue ($)': [60000, 100000, 90000, 120000, 110000, 80000, 130000, 100000, 110000, 90000, 60000, 80000], 'Expenses ($)': [45000, 75000, 65000, 90000, 80000, 70000, 95000, 75000, 80000, 65000, 45000, 70000], 'Profit ($)': [15000, 25000, 25000, 30000, 30000, 10000, 35000, 25000, 30000, 25000, 15000, 10000]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set parameters for the figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df.index, df['Investment ($)'], df['Revenue ($)'], df['Expenses ($)'], df['Profit ($)'], labels=['Investment', 'Revenue', 'Expenses', 'Profit'], colors=['#FFB6C1', '#87CEEB', '#FFDAB9', '#90EE90'], alpha=0.8)

# Set x and y axis ticks and labels
ax.set_xticks(df.index)
ax.set_xticklabels(df['Sector'], rotation=45, ha='right', rotation_mode='anchor')

# Calculate max total value and set y axis ticks and labels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(axis='y', linestyle='--')

# Set legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='upper left')

# Set title and labels
ax.set_title('Business Performance across Different Sectors')
ax.set_xlabel('Sector')
ax.set_ylabel('Amount ($)')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_22.png', bbox_inches='tight')

# Clear current image state
plt.clf()