



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Import seaborn as sns
import seaborn as sns

# Set the data
data = {'Organization': ['Red Cross', 'Habitat for Humanity', 'Doctors Without Borders', 'Feeding America', 'World Wildlife Fund'],
        'Total Revenue ($)': [50, 30, 80, 55, 40],
        'Expenses on Program Services ($)': [40, 25, 75, 50, 35],
        'Expenses on Fundraising ($)': [5, 2, 5, 3, 3],
        'Expenses on Administration ($)': [5, 3, 5, 2, 2],
        'Fundraising Efficiency (%)': [80, 85, 90, 85, 90],
        'Admin Efficiency (%)': [90, 70, 90, 95, 95]}

# Convert the data into a pandas dataframe
df = pd.DataFrame(data)

# Set the index to be the organization names
df = df.set_index('Organization')

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the heatmap using seaborn
sns.heatmap(df, annot=True, cmap='Blues', cbar=True)

# Set the ticks and ticklabels for the x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set the ticks to be in the center of the cells
ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=False)

# Add a title
plt.title('Financial Performance of Charities')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-134212_97.png', bbox_inches='tight')

# Clear the current image state
plt.clf()