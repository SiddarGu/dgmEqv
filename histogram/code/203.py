import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Given data
data = np.array([
    [55], [65], [75], [82], [88], [90], [92], [94], [95]
])

data_labels = ['Number of Tourists (Thousands)', 'Hotel Occupancy Rate (%)']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450']

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels[1:])

# Setting the larger figsize to prevent content from being cut off.
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Create the histogram
ax = sns.barplot(x=df.index, y=df['Hotel Occupancy Rate (%)'], palette="viridis")

# Set the title of the figure
ax.set_title('Relationship Between Tourist Numbers and Hotel Occupancy Rates')

# If the text length of the label is too long, rotate the labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# Automatically resize the image
plt.tight_layout()

# Save the image to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/203.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
