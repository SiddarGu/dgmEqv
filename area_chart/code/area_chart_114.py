
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Year': ['2017', '2018', '2019', '2020', '2021'],
        'Online Sales ($)': [100000, 120000, 150000, 180000, 210000],
        'In-store Sales ($)': [120000, 140000, 160000, 180000, 200000],
        'Total Sales ($)': [220000, 260000, 310000, 360000, 410000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with an area chart using ax.stackplot()
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df['Year'], df['Online Sales ($)'], df['In-store Sales ($)'], df['Total Sales ($)'], labels=['Online Sales', 'In-store Sales', 'Total Sales'], colors=['#56B4E9', '#E69F00', '#009E73'], alpha=0.7)

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000)

# Set x and y axis ticks and ticklabels
if np.random.rand() <= 0.7: # 70% probability of setting ticks and ticklabels
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
    ax.set_yticks(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(ax.get_yticks(), rotation=0, ha='right', rotation_mode='anchor')
else: # If not setting ticks and ticklabels, hide them
    ax.tick_params(axis='both', which='both', length=0)

# Set grid lines
ax.grid(linestyle='dotted', linewidth=0.5, color='grey', alpha=0.5)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), framealpha=0)

# Set title
ax.set_title('Retail and E-commerce Sales Trends by Year')

# Automatically resize image
fig.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-140159_23.png', bbox_inches='tight')

# Clear the current image state
plt.clf()