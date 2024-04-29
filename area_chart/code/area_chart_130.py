
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Public Transportation (Funding)': [3000, 3500, 4000, 4500, 5000],
        'Education (Funding)': [5000, 5500, 6000, 6500, 7000],
        'Healthcare (Funding)': [4000, 4500, 5000, 5500, 6000],
        'Infrastructure (Funding)': [6000, 6500, 7000, 7500, 8000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10,6))

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df)))
ax.set_xticklabels(df.iloc[:, 0])
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--')

# Calculate max total value and set suitable ylim range
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value > 1000:
    max_total_value = np.ceil(max_total_value / 1000) * 1000
elif max_total_value > 100:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)

# Plot data using area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=['Public Transportation (Funding)', 'Education (Funding)', 'Healthcare (Funding)', 'Infrastructure (Funding)'], colors=['#4c72b0', '#55a868', '#c44e52', '#8172b2'], alpha=0.7)

# Set legend position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title
ax.set_title('Government Funding Allocation by Sector from 2015 to 2019')

# Automatically resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_44.png', bbox_inches='tight')

# Clear current image state
plt.clf()
plt.close()