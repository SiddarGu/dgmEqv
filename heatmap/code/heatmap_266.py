
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {'Energy Source': ['Coal (MW)', 'Natural Gas (MW)', 'Nuclear (MW)', 'Renewables (MW)', 'Hydro (MW)', 'Oil (MW)'],
        'United States': [4000, 6000, 2500, 3500, 2000, 1000],
        'China': [6000, 8000, 4000, 5000, 3000, 1500],
        'India': [3500, 4500, 2000, 3000, 1500, 750],
        'Japan': [2000, 2500, 1000, 1500, 800, 500],
        'Germany': [2500, 3500, 1500, 2000, 1000, 500],
        'United Kingdom': [2000, 3000, 1000, 1500, 800, 400]}

# Create pandas dataframe
df = pd.DataFrame(data)

# Set Energy Source as index
df.set_index('Energy Source', inplace=True)

# Plot heatmap chart using seaborn
plt.figure(figsize=(12, 8))
sns.heatmap(df, annot=True, fmt='d', cmap='Blues', cbar=False)

# Set ticks and labels for x and y axis
plt.xticks(np.arange(6)+0.5, df.columns, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(6)+0.5, df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set title and labels
plt.title('Energy Sources by Country')
plt.xlabel('Country')
plt.ylabel('Energy Source')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-162116_20.png', bbox_inches='tight')

# Clear current image state
plt.clf()