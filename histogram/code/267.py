import pandas as pd
import matplotlib.pyplot as plt

# Data Preparation
data_labels = ['Yield (million metric tons)']
line_labels = ['Wheat', 'Rice', 'Corn', 'Barley', 'Soybean', 'Sorghum', 'Oats', 'Rye']
data = [65.3, 80.7, 90.1, 25.8, 55.2, 35.6, 18.5, 9.2]

# Convert the data into a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create the figure and a subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plotting the data
df.plot(kind='barh', ax=ax, legend=False, color='skyblue')

# Setting the title of the histogram
plt.title('Global Crop Yields in Agriculture and Food Production')

# Adding grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Rotate the y-axis labels if necessary to prevent overlapping
plt.yticks(wrap=True)

# Customize the plot to look fancy
ax.set_facecolor('#f0f0f0')  # Setting the background color for the plot area
for spine in ax.spines.values():
    spine.set_visible(False)

# Adjust the layout to make sure everything fits without overlap
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/617.png'
plt.savefig(save_path)

# Clear the current figure's state
plt.clf()
