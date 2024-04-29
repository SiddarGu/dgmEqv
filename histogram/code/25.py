import pandas as pd
import matplotlib.pyplot as plt

# Data processing
data_labels = ['Number of Visitors (Thousands)']
line_labels = ['0-18', '19-30', '31-45', '46-60', '61+']
data = [15, 30, 25, 20, 10]

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Visualization
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Creating the histogram with background grid & fancy colors
df[data_labels[0]].plot(kind='bar', color=plt.cm.viridis(range(len(data))), ax=ax)

# Set the title of the figure
plt.title('Age Distribution of Visitors at Arts Exhibitions')

# Set the rotation for the x-axis labels to prevent overlapping
plt.xticks(rotation=45, ha='right')

# Setting up the grid, labels and legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('Age Range')
plt.ylabel(data_labels[0])

# Use tight_layout to fit the axes within the figure neatly
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/25.png'
plt.savefig(save_path)

# Clear the current figure
plt.clf()
