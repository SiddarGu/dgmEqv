
import matplotlib.pyplot as plt
import numpy as np

data = {
    "Painting": [50, 125, 200, 275, 350],
    "Music": [80, 150, 220, 280, 370],
    "Dance": [20, 60, 100, 140, 200],
    "Theater": [90, 160, 240, 310, 400],
    "Photography": [30, 90, 150, 210, 300]
}

outliers = {
    "Music": [450],
    "Theater": [450, 500],
    "Photography": [350]
}

# Create figure
fig = plt.figure(figsize=(8,4))

# Loop over each category
for i, category in enumerate(data.keys()):

    # Add subplot
    ax = fig.add_subplot(1,5,i+1)

    # Set title
    ax.set_title(category)
  
    # Set grids
    ax.grid(linestyle='dotted', linewidth=2, color='black')

    # Get data for plotting
    x_data = list(data.keys())
    y_data = data[category]

    # Plot data
    bp = ax.boxplot(y_data, vert=False, patch_artist=True, showmeans=True)

    # Set color
    for patch, color in zip(bp['boxes'], ['darkorange']):
        patch.set_facecolor(color)

    # Plot outliers
    if category in outliers.keys():
        for outlier in outliers[category]:
            ax.plot(outlier, 1, 'go')

# Set figure title
fig.suptitle("Cost of Arts and Culture Activities in 2021")

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/13_202312251044.png")

# Clear the current image state
plt.clf()