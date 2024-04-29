import matplotlib.pyplot as plt
import numpy as np
import os

# Transforming given data into variables
data_labels = ['Annual Sales (Billion USD)']
line_labels = ['Carbonated Soft Drinks', 'Bottled Water',
               'Sports and Energy Drinks', 'Coffee and Tea',
               'Alcoholic Beverages', 'Dairy-Based Beverages', 'Plant-Based Milks']
data = [29.6, 18.5, 14.3, 12.9, 26.7, 11.4, 9.5]

# Set the figsize
plt.figure(figsize=(14, 8))

# Plotting the histogram
ax = plt.subplot(111)
bars = ax.bar(line_labels, data, color=plt.cm.tab10(np.arange(len(data))))

# Adding grids in the background
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Rotate the labels if they are too long
plt.xticks(rotation=45, ha='right')

# Set the title
plt.title('Annual Sales by Beverage Type in Food and Beverage Industry')

# Make the plot layout clear and well-sized
plt.tight_layout()

# Save the figure to the specific path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/229.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure's state
plt.clf()
