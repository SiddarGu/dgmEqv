
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define data dictionary
data = {'Category': ['Technology', 'Retail', 'Healthcare', 'Finance', 'Education'],
        'Total Revenue ($)': [500000, 600000, 300000, 800000, 400000],
        'Operating Expenses ($)': [350000, 400000, 250000, 550000, 300000],
        'Net Profits ($)': [150000, 200000, 50000, 250000, 100000],
        'Assets ($)': [1000000, 1200000, 800000, 1500000, 500000],
        'Liabilities ($)': [300000, 400000, 200000, 500000, 250000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot area chart
ax.stackplot(df['Category'], df['Total Revenue ($)'], df['Operating Expenses ($)'], df['Net Profits ($)'], df['Assets ($)'], df['Liabilities ($)'], labels=['Total Revenue', 'Operating Expenses', 'Net Profits', 'Assets', 'Liabilities'], colors=['#5E9DC8', '#E89F41', '#8FCC71', '#D77A7A', '#B782E1'], alpha=0.7)

# Set ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(len(df['Category'])))
    ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_xlim(0, len(df.index) - 1)
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
else:
    ax.set_xticks([])
    ax.set_yticks([])

# Set ylimit and yticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(color='gray', linestyle='dashed', alpha=0.5)

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Financial Performance by Industry')

# Automatically resize image
fig.tight_layout()

# Save image
fig.savefig('output/final/area_chart/png/20231228-140159_34.png', bbox_inches='tight')

# Clear figure
plt.clf()