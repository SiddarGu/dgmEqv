


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Create a dictionary for the data
data = {'Country': ['China', 'United States', 'India', 'Russia', 'Japan'],
        'Carbon Emissions (Million Metric Tons)': [10, 5, 3, 4, 2],
        'Energy Consumption (Billion Kilowatt Hours)': [500, 350, 300, 200, 150],
        'Renewable Energy (%)': [20, 15, 10, 25, 30],
        'Water Usage (Billion Cubic Meters)': [200, 150, 100, 50, 75],
        'Waste Production (Million Metric Tons)': [1000, 800, 600, 400, 300]}

# Create a dataframe from the dictionary
df = pd.DataFrame(data)

# Set the figure size
fig = plt.figure(figsize=(10, 8))

# Create a heatmap chart using seaborn
ax = sns.heatmap(df.iloc[:, 1:], annot=True, fmt='g', cmap='Blues',
                 cbar_kws={'label': 'Value'})

# Set the title of the figure
plt.title('Environmental Impact by Country')

# Set the label for the x and y axis
plt.xlabel('Category')
plt.ylabel('Country')

# Set the ticks and ticklabels for the x and y axis
plt.xticks(np.arange(5) + 0.5, df.columns[1:], rotation=45, ha='right',
           rotation_mode='anchor')
plt.yticks(np.arange(5) + 0.5, df['Country'], rotation=0, ha='right')

# Automatically resize the image before saving
plt.tight_layout()

# Save the figure as a png file
plt.savefig('output/final/heatmap/png/20231228-124154_5.png', bbox_inches='tight')

# Clear the current image state
plt.clf()