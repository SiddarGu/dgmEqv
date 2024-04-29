
# Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Process the data
data_dict = {'Type of Law': ['Criminal', 'Family', 'Corporate', 'Immigration', 'Real Estate', 'Intellectual Property'],
             'Lawyer Count': [100, 200, 300, 150, 50, 100]}
data_df = pd.DataFrame(data_dict)

# Set figure size
fig = plt.figure(figsize=(10,8))

# Plot the heatmap chart
ax = plt.subplot()
heatmap = ax.imshow(data_df['Lawyer Count'].values.reshape(1,6), cmap='BuPu')

# Add x and y ticks and tick labels
ax.set_xticks(np.arange(6))
ax.set_xticklabels(data_df['Type of Law'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticks(np.arange(1))
ax.set_yticklabels(['Lawyer Count'])

# Add value text to each cell
for i in range(1):
    for j in range(6):
        text = ax.text(j, i, data_df['Lawyer Count'].iloc[j], ha='center', va='center', color='w')

# Add colorbar
plt.colorbar(heatmap)

# Add title
plt.title('Distribution of Lawyers by Law Type')

# Automatically resize the image and save
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_36.png', bbox_inches='tight')

# Clear the current image state
plt.clf()