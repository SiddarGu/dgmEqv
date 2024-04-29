import matplotlib.pyplot as plt
import numpy as np
import os

# Define the data
data_labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
data = np.array([45, 38, 32, 25, 20, 15, 10, 5, 3, 2])
line_labels = ['Carbon Emission Reduction (Million Metric Tons)', 'Number of Projects']

# Create a new figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Plotting the histogram
ax.barh(data_labels, data, color='skyblue', edgecolor='black')

# Add grid lines behind the bars
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')

# Setting the title of the histogram
ax.set_title('Impact of Sustainability Projects on Carbon Emission Reduction')

# Rotate the labels if they are too long
plt.xticks(rotation=45)
plt.yticks(wrap=True)

# Set xlabel and ylabel
ax.set_xlabel(line_labels[1])
ax.set_ylabel(line_labels[0])

# Automatically adjust the layout to prevent content from being cut off
plt.tight_layout()

# Saving the figure to the specified path
output_dir = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
plt.savefig(f'{output_dir}/140.png', format='png')

# Clear the current image state
plt.clf()
