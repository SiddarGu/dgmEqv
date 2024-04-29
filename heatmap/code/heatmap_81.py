
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Process the data using dict and pandas
data = {'Product':['Product A', 'Product B', 'Product C', 'Product D', 'Product E'], 
        'Production Speed (units per hour)':[100, 85, 75, 110, 120], 
        'Quality Control (%)':[95, 90, 85, 98, 99], 
        'Downtime (hours)':[2, 4, 6, 1, 0.5], 
        'Waste (%)':[3, 5, 8, 2, 1], 
        'Efficiency (%)':[98, 95, 90, 99, 99.5]}

df = pd.DataFrame(data)
df.set_index('Product', inplace=True)

# Plot the data with heatmap chart
fig, ax = plt.subplots(figsize=(12,6))
ax = sns.heatmap(df, annot=True, fmt='.1f', cmap='Blues', linewidths=.5, cbar=True, cbar_kws={"shrink": .5})

# Set the ticks and ticklabels for x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)

# Set the title
ax.set_title('Manufacturing Efficiency Metrics')

# Automatically resize the image
fig.tight_layout()

# Save the image
fig.savefig('output/final/heatmap/png/20231228-124154_72.png', bbox_inches='tight')

# Clear the current image state
plt.clf()

# Check the generated code to make sure it doesn't report errors and save path is correct