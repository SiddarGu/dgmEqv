
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
data = {'Year': ['2018', '2019', '2020', '2021', '2022'],
        'Education ($)': [5000, 5500, 6000, 6500, 7000],
        'Infrastructure ($)': [6000, 6500, 7000, 7500, 8000],
        'Healthcare ($)': [4000, 4500, 5000, 5500, 6000],
        'Public Safety ($)': [3000, 3500, 4000, 4500, 5000],
        'Social Programs ($)': [2000, 2500, 3000, 3500, 4000]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Ceil up to nearest multiple of 10, 100 or 1000
if max_total_value <= 10:
    max_total_value = np.ceil(max_total_value)
elif max_total_value <= 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value <= 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y limit and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot data as stacked area chart
ax.stackplot(df['Year'], df['Education ($)'], df['Infrastructure ($)'], df['Healthcare ($)'],
             df['Public Safety ($)'], df['Social Programs ($)'], labels=['Education', 'Infrastructure', 'Healthcare', 'Public Safety', 'Social Programs'])

# Set x limit and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')

# Set legend
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left')

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--')

# Set title
ax.set_title('Government Expenditure Analysis')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-145339_73.png', bbox_inches='tight')

# Clear current image state
plt.clf()