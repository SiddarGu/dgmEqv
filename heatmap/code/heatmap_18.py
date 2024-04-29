
# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define data as a dictionary
data = {
    'Country': ['USA', 'UK', 'Canada', 'Australia', 'Germany'],
    'Education': [30, 25, 10, 20, 15],
    'Healthcare': [25, 40, 15, 10, 10],
    'Transportation': [20, 25, 30, 15, 10],
    'Taxation': [20, 20, 25, 30, 5],
    'Social Services': [15, 10, 20, 10, 45]
}

# Convert data into a pandas DataFrame
df = pd.DataFrame(data)

# Set Policy Area as the index
df.set_index('Country', inplace=True)

# Set figsize to a larger setting to prevent content from being displayed
plt.figure(figsize=(10, 8))

# Plot the heatmap using sns.heatmap()
sns.heatmap(df, annot=True, cmap='Blues')

# Set the title of the figure
plt.title('Government Spending by Policy Area')

# Set the ticks and ticklabels for x and y axis, and make them in the center of rows and columns
plt.xticks(np.arange(5) + 0.5, df.columns, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(5) + 0.5, df.index, rotation=0)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image as a png file
plt.savefig('output/final/heatmap/png/20231226-140552_10.png', bbox_inches='tight')

# Clear the current image state
plt.clf()