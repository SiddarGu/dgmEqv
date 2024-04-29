
# Import the necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary to store the data
data = {'Subject Name': ['Mathematics', 'Science', 'English', 'History', 'Art', 'Physical Education'],
        'High School': [95, 88, 75, 82, 65, 90],
        'College': [85, 92, 90, 75, 80, 95],
        'Graduate School': [70, 78, 95, 90, 85, 80]}

# Convert the dictionary into a pandas dataframe
df = pd.DataFrame(data)

# Set the index to be the 'Subject Name' column
df = df.set_index('Subject Name')

# Create a figure with a larger figsize
fig = plt.figure(figsize=(10, 8))

# Plot the data as a heatmap chart using imshow()
ax = fig.add_subplot()
im = ax.imshow(df, cmap='Blues')

# Add a colorbar to the chart
cbar = fig.colorbar(im, ax=ax)

# Set the ticks and ticklabels for the x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))

ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# Set the ticks and ticklabels in the center of rows and columns
ax.tick_params(axis='x', bottom=False, labelbottom=False, top=True, labeltop=True)
ax.tick_params(axis='y', left=False, labelleft=False, right=True, labelright=True)

# Add the value of each cell as text
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='black')

# Set the title of the figure
plt.title('Performance in Academic Subjects by Education Level')

# Automatically resize the image and savefig
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231225-210514_1.png', bbox_inches='tight')

# Clear the current image state
plt.clf()