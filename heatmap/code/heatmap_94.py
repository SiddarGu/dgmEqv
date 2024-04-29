
# Import necessary packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create a dictionary to store the data
data = {'Category': ['Sociology', 'Psychology', 'Political Science', 'History', 'Economics', 'Anthropology'],
        'Research and Development (%)': [25, 20, 15, 10, 5, 0],
        'Data Collection (%)': [30, 25, 20, 15, 10, 5],
        'Data Analysis (%)': [35, 30, 25, 20, 15, 10],
        'Publication (%)': [40, 35, 30, 25, 20, 15],
        'Collaboration (%)': [45, 40, 35, 30, 25, 20]}

# Convert the data into a Pandas dataframe
df = pd.DataFrame(data)

# Set the figure size to a larger setting
plt.figure(figsize=(12, 7))

# Use seaborn to create a heatmap chart
ax = sns.heatmap(df.set_index('Category'), annot=True, cmap='BuPu')

# Set the tick labels and ticks to the center of rows and columns
# ax.set_xticklabels(df.columns[1:], ha='center')
# ax.set_yticklabels(df['Category'], va='center')

# Set the rotation of the x-axis labels to 45 degrees
# plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Set the title of the figure
plt.title('Research Process in Social Sciences')

# Automatically resize the image
plt.tight_layout()

# Save the figure as a png file
plt.savefig('output/final/heatmap/png/20231228-124154_92.png', bbox_inches='tight')

# Clear the current figure state
plt.clf()