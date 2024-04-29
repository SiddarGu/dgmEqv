
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary from the given data
data = {'Country': ['United States', 'China', 'Japan', 'Germany', 'United Kingdom'], 
        'Population (Millions)': [330, 1400, 126, 83, 67], 
        'GDP (Trillion USD)': [20, 16, 5, 4, 3], 
        'Healthcare Spending (% of GDP)': ['18%', '20%', '22%', '25%', '18%'], 
        'Education Spending (% of GDP)': ['10%', '15%', '20%', '15%', '17%'], 
        'Military Spending (% of GDP)': ['5%', '10%', '15%', '20%', '25%']}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame.from_dict(data)

# Set the index to be the Country column
df = df.set_index('Country')

# Convert the percentage columns to numeric values
df['Healthcare Spending (% of GDP)'] = df['Healthcare Spending (% of GDP)'].str.replace('%', '').astype(float) / 100
df['Education Spending (% of GDP)'] = df['Education Spending (% of GDP)'].str.replace('%', '').astype(float) / 100
df['Military Spending (% of GDP)'] = df['Military Spending (% of GDP)'].str.replace('%', '').astype(float) / 100

# Set the figure size to be larger
plt.figure(figsize=(10,8))

# Plot the heatmap using imshow()
plt.imshow(df, cmap='Blues')

# Set the x and y ticks and tick labels
plt.xticks(np.arange(len(df.columns)), df.columns, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(len(df.index)), df.index)

# Set the ticks and tick labels to be in the center of rows and columns
plt.tick_params(axis='both', labelbottom=True, bottom=True, top=False, labeltop=False, labelleft=False, direction='inout')
plt.tick_params(axis='x', labelbottom=True, bottom=False, top=True, labeltop=True, labelleft=False, direction='inout')
plt.tick_params(axis='y', labelleft=True, left=False, right=True, labelright=True, labelbottom=False, direction='inout')

# Add a colorbar
plt.colorbar()

# Automatically resize the image
plt.tight_layout()

# Set the title 
plt.title('Country Comparison of Government Spending')

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-124154_97.png', bbox_inches='tight')

# Clear the current image state
plt.clf()