



            
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set the data
data = {'Industry': ['Technology', 'Finance', 'Retail', 'Healthcare', 'Energy'],
        'Revenue (in millions)': [25000, 30000, 20000, 35000, 40000],
        'Profit Margin (%)': [20, 15, 18, 25, 10],
        'Assets (in millions)': [50000, 40000, 35000, 40000, 60000],
        'Debt (in millions)': [25000, 30000, 20000, 35000, 40000]}

# Convert data into a pandas dataframe
df = pd.DataFrame(data)

# Set the index of the dataframe to the "Industry" column
df.set_index('Industry', inplace=True)

# Create a figure and axes object
fig, ax = plt.subplots(figsize=(10, 6))

# Use seaborn heatmap to plot the data
sns.heatmap(df, annot=True, fmt='.0f', cmap='Blues', cbar=False)

# Set the x and y ticks and labels
ax.set_xticks(np.arange(len(df.columns))+0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticks(np.arange(len(df.index))+0.5)
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor', wrap=True)
ax.tick_params(axis='both', which='both', length=0)

# Set the title of the figure
plt.title('Industry Performance Metrics')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-131639_66.png', bbox_inches='tight')

# Clear the current image state
plt.clf()