

import matplotlib.pyplot as plt 
import numpy as np 

Destination = ['USA', 'UK', 'Germany', 'France']
Hotels = [500, 600, 400, 450]
Restaurants = [800, 900, 700, 750]
Attractions = [1000, 1200, 900, 1100]  

# Create a figure
fig = plt.figure(figsize=(10, 8))

# Create subplots
ax = fig.add_subplot(111)

# Set the width of each bar
width = 0.2

# Plot the data
ax.bar(Destination, Hotels, width, label='Hotels')
ax.bar(np.arange(len(Destination))+width, Restaurants, width, label='Restaurants')
ax.bar(np.arange(len(Destination))+width*2, Attractions, width, label='Attractions')

# Add title and axes labels
ax.set_title('Number of hotels, restaurants and attractions in four countries in 2021')
ax.set_xlabel('Destination')
ax.set_ylabel('Number')

# Add legend
ax.legend()

# Place labels on the bars
for idx,rect in enumerate(ax.patches):
    # Get X and Y placement of label from rect
    y_value = rect.get_height()
    x_value = rect.get_x() + rect.get_width()/2
    # Number of points between bar and label
    space = 5
    # Vertical alignment for positive values
    ha = 'center'
    # If value of bar is negative: Place label below bar
    if y_value < 0:
        # Invert space to place label below
        space *= -1
        # Vertically align label at top
        ha = 'top'
    # Use Y value as label and format number with one decimal place
    label = "{:.1f}".format(y_value)
    # Create annotation
    ax.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(0, space),          # Vertically shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        ha=ha,                      # Horizontally center label
        rotation=90)                # Rotate label

# Automatically resize the image by tight_layout
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/68.png')

# Clear the current state of the image
plt.clf()