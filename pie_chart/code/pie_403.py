

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.set_title("Distribution of Arts in the World, 2023")
ax.set_xlabel("Arts")
ax.set_ylabel("Percentage")

# Set the x-axis and y-axis limits
ax.set_xlim(0, 5)
ax.set_ylim(0, 100)

# Specify the category order
x_labels = ["Visual Arts", "Music", "Literature", "Theatre", "Film", "Dance"]

# Plot bars
ax.bar(x_labels,
        [25, 20, 20, 15, 10, 10],
        color=['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#00B2FF'])

# Set text label and properties
rects = ax.patches
labels = [25, 20, 20, 15, 10, 10]

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 1, label,
            ha='center', va='bottom', fontsize=20, rotation=0, wrap=True)

# Use tight_layout to make sure the text fits
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/226.png')

# Clear the current image
plt.cla()