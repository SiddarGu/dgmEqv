
# Import required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define the data as a dictionary
data = {'Factory': ['Factory A', 'Factory B', 'Factory C', 'Factory D', 'Factory E'],
        'Production (Units)': [500, 450, 600, 550, 400],
        'Defect Rate (%)': [2, 3, 2.5, 2.5, 3],
        'Downtime (Hours)': [20, 25, 15, 18, 30],
        'Efficiency (%)': [95, 90, 93, 92, 88],
        'Waste (Units)': [15, 20, 18, 16, 22],
        'Cost per Unit ($)': [1.50, 1.75, 1.60, 1.65, 1.80]}

# Convert the data into a pandas dataframe
df = pd.DataFrame(data)

# Set the figure size
fig, ax = plt.subplots(figsize=(8, 6))

# Use seaborn heatmap to plot the data
sns.heatmap(df.iloc[:, 1:], annot=True, fmt='.2f', cmap='Blues', cbar=False)

# Set the title and axis labels
ax.set_title('Key Performance Indicators in Manufacturing')
ax.set_xlabel('Metrics')
ax.set_ylabel('Factory')

# Set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(6) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(5) + 0.5)
ax.set_yticklabels(df['Factory'], rotation=0, ha='right', rotation_mode='anchor')

# Use tight_layout to automatically resize the image
plt.tight_layout()

# Save the figure as a png file
plt.savefig('output/final/heatmap/png/20231228-124154_34.png', bbox_inches='tight')

# Clear the current image state
plt.clf()