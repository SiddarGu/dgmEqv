
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary with the data
data = {
    'Organization': ['Red Cross', 'Salvation Army', 'Doctors Without Borders', 'UNICEF', 'Habitat for Humanity'],
    'Revenue (Millions)': [150, 125, 100, 175, 75],
    'Expenses (Millions)': [100, 80, 70, 120, 50],
    'Total Assets (Millions)': [200, 175, 150, 220, 100],
    'Program Expenses (%)': [75, 80, 85, 70, 90],
    'Fundraising Expenses (%)': [10, 15, 10, 20, 5],
    'Administrative Expenses (%)': [15, 5, 5, 10, 5]
}

# Use pandas to create a dataframe
df = pd.DataFrame(data)

# Set the columns as the index for the dataframe
df.set_index('Organization', inplace=True)

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the heatmap
heatmap = ax.imshow(df, cmap='plasma')

# Add a colorbar
if np.random.choice([True, False], p=[0.4, 0.6]):
    fig.colorbar(heatmap, ax=ax)

# Add labels for the cells
if np.random.choice([True, False], p=[0.4, 0.6]):
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='w')

# Set the ticks and ticklabels for the x-axis
ax.set_xticks(np.arange(df.shape[1]))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# Set the ticks and ticklabels for the y-axis
ax.set_yticks(np.arange(df.shape[0]))
ax.set_yticklabels(df.index, ha='center', rotation=0)

# Set the labels for the axes
ax.set_xlabel('Financial Data')
ax.set_ylabel('Organization')

# Set the title for the figure
ax.set_title('Financial Performance of Major Charities')

# Automatically resize the image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_43.png', bbox_inches='tight')

# Clear the current image state
plt.clf()