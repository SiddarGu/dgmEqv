
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import seaborn as sns

# Define the data
data = {
    'Country': ['United States', 'China', 'India', 'Brazil', 'Russia', 'France'],
    'Wheat (Tonnes per Hectare)': [3.2, 4.5, 2.8, 3.6, 2.2, 3.1],
    'Corn (Tonnes per Hectare)': [5.5, 6.8, 4.5, 5.2, 4.0, 4.8],
    'Rice (Tonnes per Hectare)': [3.0, 5.1, 2.8, 3.8, 2.5, 3.2],
    'Soybeans (Tonnes per Hectare)': [2.5, 3.9, 2.2, 3.1, 2.0, 2.8],
    'Barley (Tonnes per Hectare)': [4.0, 5.2, 3.5, 4.2, 3.0, 2.8],
    'Potatoes (Tonnes per Hectare)': [6.1, 7.5, 4.8, 5.5, 4.2, 5.2]
}

# Create a pandas dataframe
df = pd.DataFrame(data)

# Set the country column as the index
df.set_index('Country', inplace=True)

# Create the heatmap
fig, ax = plt.subplots(figsize=(10, 7))
sns.heatmap(df, annot=True, cmap='YlGnBu', cbar=False, ax=ax)

# Set the tick positions and labels for the x and y axis
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set the tick positions to be in the center of rows and columns
ax.tick_params(axis='both', which='both', length=0)
ax.xaxis.set_major_locator(ticker.IndexLocator(base=1, offset=0.5))
ax.yaxis.set_major_locator(ticker.IndexLocator(base=1, offset=0.5))

# Set the title
plt.title('Crop Yields by Country')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_2.png', bbox_inches='tight')

# Clear the current image state
plt.clf()