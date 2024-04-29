
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import data
data = {'City': ['New York', 'Paris', 'London', 'Tokyo', 'Dubai'], 
        'Hotel Bookings (in millions)': [25.3, 20.5, 18.2, 15.1, 10.5], 
        'Tourist Arrivals (in millions)': [30.5, 26.8, 23.4, 19.5, 15.8], 
        'Revenue per Available Room (in USD)': [175, 200, 225, 250, 300], 
        'Average Length of Stay (in nights)': [5, 4, 3, 2, 4], 
        'Tourism Contribution to GDP (%)': [15, 20, 25, 30, 35]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set index as City
df.set_index('City', inplace=True)

# Create figure and axes
fig, ax = plt.subplots(figsize=(8,6))

# Plot heatmap using imshow()
im = ax.imshow(df, cmap='Blues', interpolation='nearest')

# Add colorbar
cbar = plt.colorbar(im, ax=ax)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Loop over data dimensions and create text annotations
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='black')

# Set title
ax.set_title('Tourism and Hospitality Statistics by City')

# Automatically resize image before saving
plt.tight_layout()

# Save figure as png
plt.savefig('output/final/heatmap/png/20231228-155147_51.png', bbox_inches='tight')

# Clear current image state
plt.clf()