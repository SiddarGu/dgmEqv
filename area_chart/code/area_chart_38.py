


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {
    'Property Type': ['1 Bedroom', '2 Bedrooms', '3 Bedrooms', '4 Bedrooms', '5+ Bedrooms'],
    'Apartment (Avg. Price)': [150000, 250000, 350000, 450000, 550000],
    'House (Avg. Price)': [200000, 300000, 400000, 500000, 600000],
    'Condo (Avg. Price)': [120000, 200000, 300000, 400000, 500000]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3],
             labels=['Apartment', 'House', 'Condo'], alpha=0.7)

# Set x and y axis ticks and ticklabels
if np.random.uniform() < 0.7:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0])

if np.random.uniform() < 0.7:
    # Calculate max total value and set suitable ylime range and yticks
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value < 10:
        yticks = [0, 10]
    elif max_total_value < 100:
        yticks = np.linspace(0, max_total_value, np.random.choice([3, 5]), dtype=np.int32)
    elif max_total_value < 1000:
        yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7]), dtype=np.int32)
    else:
        yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
    
    ax.set_ylim(0, yticks[-1])
    ax.set_yticks(yticks)

# Set background grid lines
if np.random.uniform() < 0.7:
    ax.grid(color='lightgrey', linestyle='--', linewidth=0.5, alpha=0.5)

# Adjust legend's position
ax.legend(loc='upper right')

# Automatically resize image before savefig
fig.tight_layout()

# Set title and ylabels
ax.set_title('Average Housing Prices by Property Type')
ax.set_ylabel('Price ($)')
ax.set_xlabel('Property Type')

# Save image with correct path and file name
plt.savefig('output/final/area_chart/png/20231228-131755_0.png', bbox_inches='tight')

# Clear current image state
plt.clf()