

            
# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Year': ['2016', '2017', '2018', '2019', '2020'], 
        'Public Education (Funding)': [5000, 5500, 6000, 6500, 7000], 
        'Healthcare (Funding)': [6000, 6500, 7000, 7500, 8000], 
        'Infrastructure (Funding)': [7000, 7500, 8000, 8500, 9000], 
        'Social Services (Funding)': [8000, 8500, 9000, 9500, 10000]}

# Use pandas to process data
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up to nearest multiple of 1000
max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y limit and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x limit and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))

# Set x and y tick labels
ax.set_xticklabels(df['Year'])
ax.set_yticklabels(['${:,}'.format(x) for x in ax.get_yticks()])

# Set title
ax.set_title('Government Expenditure on Public Services from 2016 to 2020')

# Plot the data using area chart
ax.stackplot(df['Year'], df['Public Education (Funding)'], df['Healthcare (Funding)'], df['Infrastructure (Funding)'], df['Social Services (Funding)'], labels=['Public Education', 'Healthcare', 'Infrastructure', 'Social Services'], colors=['skyblue', 'lightgreen', 'orange', 'pink'], alpha=0.7)

# Set background grid lines
ax.grid(color='gray', linestyle='--', linewidth=1, alpha=0.3)

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_79.png', bbox_inches='tight')

# Clear current image state
plt.clf()