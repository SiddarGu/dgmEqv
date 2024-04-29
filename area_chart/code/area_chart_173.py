
       
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Prepare data
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'], 
        'Single Family Home Sales (Units)': [2000, 1500, 1000, 2500], 
        'Condo Sales (Units)': [3000, 2500, 2000, 1500], 
        'Rentals (Units)': [2500, 2000, 1500, 3000]}
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

# Plot the data as an area chart
ax.stackplot(df['City'], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3],
             labels=df.columns[1:], alpha=0.5)

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)

# Set x and y axis ticks and tick labels
ax.set_xticks(np.arange(len(df['City'])))
ax.set_xticklabels(df['City'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5)

# Add legend
ax.legend(loc='upper right')

# Set title and axes labels
ax.set_title('Real Estate Market Statistics in Major Cities')
ax.set_xlabel('City')
ax.set_ylabel('Units/Percentage')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_93.png', bbox_inches='tight')

# Clear current image state
plt.clf()