
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data as a dictionary
data = {'Category Name': ['Retail', 'Technology', 'Finance', 'Healthcare', 'Energy'],
        'Revenue (Millions)': [500, 800, 1000, 600, 400],
        'Net Income (Millions)': [100, 200, 300, 150, 50],
        'Total Assets (Millions)': [1000, 1500, 2000, 1200, 800],
        'Total Liabilities (Millions)': [700, 900, 1200, 800, 600]}

# Convert data into a dataframe
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot heatmap chart
hm = ax.imshow(df.iloc[:, 1:], cmap='Blues')

# Add x and y ticks and labels
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Category Name'])))

ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Category Name'])

# Set ticks and ticklabels in the center of rows and columns
ax.tick_params(axis='both', which='both', length=0)
ax.set_xticks(np.arange(len(df.columns[1:]))+0.5, minor=True)
ax.set_yticks(np.arange(len(df['Category Name']))+0.5, minor=True)
ax.tick_params(axis='x', which='minor', bottom=False, labelbottom=False)
ax.tick_params(axis='y', which='minor', left=False, labelleft=False)

# Set title
ax.set_title('Company Financial Performance in Various Industries')

# Add colorbar
cbar = plt.colorbar(hm, ax=ax)
cbar.ax.set_ylabel('Millions of [Currency Abbreviation]', rotation=-90, va='bottom')

# Add text to each cell
for i in range(len(df['Category Name'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j+1],
                       ha='center', va='center', color='black')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-124154_95.png', bbox_inches='tight')

# Clear the current image state
plt.clf()