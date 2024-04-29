
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
data = {'Country': ['United States', 'China', 'Germany', 'India', 'Japan'],
        'Electricity Generation (MW)': [1000, 850, 600, 750, 600],
        'Renewable Energy Generation (MW)': [500, 450, 300, 400, 350],
        'Energy Efficiency (MW)': [350, 300, 250, 300, 275],
        'Waste Management (Tons)': [100000, 95000, 80000, 90000, 85000],
        'Water Conservation (Litres)': [50000, 45000, 40000, 45000, 42500]}

# Convert data into dataframe
df = pd.DataFrame(data)

# Set country as index
df = df.set_index('Country')

# Create heatmap chart
fig, ax = plt.subplots(figsize=(10,8)) # Set figure size
heatmap = sns.heatmap(df, cmap='YlGnBu', annot=True, fmt='.0f', linewidths=.5, ax=ax) # Create heatmap with seaborn

# Set ticks and labels for x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor') # Set x-axis ticks and labels
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor') # Set y-axis ticks and labels

# Center ticks and labels
ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=False) # Set x-axis ticks to center of columns
ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=False) # Set y-axis ticks to center of rows

# Set title
ax.set_title('Sustainable Practices by Country')

# Automatically resize image
plt.tight_layout() # Automatically adjust subplot parameters
plt.savefig('./output/final/heatmap/png/20231228-163105_21.png', bbox_inches='tight') # Save figure
plt.close() # Clear current image state