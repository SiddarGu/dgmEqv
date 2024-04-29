
# Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set the data
data = {'Technology': ['USA', 'China', 'Japan', 'Germany', 'South Korea'],
        'Artificial Intelligence': [40, 35, 30, 25, 20],
        'Robotics': [35, 30, 25, 20, 18],
        'Nanotechnology': [28, 25, 20, 18, 15],
        'Biomedical Engineering': [25, 22, 18, 15, 12],
        'Environmental Science': [20, 18, 15, 12, 10]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set the index to be the countries
df.set_index('Technology', inplace=True)

# Plot the heatmap
fig, ax = plt.subplots(figsize=(10, 7))
heatmap = sns.heatmap(df, annot=True, cmap='Blues', cbar=True)

# Set the ticks and ticklabels for x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)

# Set the title and labels
plt.title('Global Advancements in Science and Engineering Fields')
plt.xlabel('Fields')
plt.ylabel('Countries')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-131639_44.png', bbox_inches='tight')

# Clear the current image state
plt.clf()