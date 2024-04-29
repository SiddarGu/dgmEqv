
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set data
data = {'Country': ['United States', 'China', 'Russia', 'Japan', 'India', 'Germany'],
        'Electricity Production (GWh)': [400000, 300000, 200000, 100000, 40000, 30000],
        'Oil Production (Millions of Barrels)': [500, 600, 400, 200, 100, 80],
        'Natural Gas Production (Trillion Cubic Feet)': [700, 800, 500, 300, 200, 150],
        'Coal Production (Millions of Short Tons)': [800, 700, 600, 400, 300, 200],
        'Renewable Energy Production (GWh)': [30000, 20000, 15000, 10000, 5000, 4000]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Set x and y labels
x_labels = ['Electricity', 'Oil', 'Natural Gas', 'Coal', 'Renewable Energy']
y_labels = ['United States', 'China', 'Russia', 'Japan', 'India', 'Germany']

# Plot heatmap
ax = sns.heatmap(df.iloc[:, 1:], annot=True, fmt='g', cmap='RdYlGn', cbar=False)

# Set ticks and ticklabels for x and y axis
ax.set_xticklabels(x_labels, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(y_labels, rotation=0)
ax.set_xticks(np.arange(0.5, 5.5, 1))
ax.set_yticks(np.arange(0.5, 6.5, 1))

# Set title
plt.title('Energy Production by Country in 2021')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-124154_87.png', bbox_inches='tight')

# Clear current image state
plt.clf()