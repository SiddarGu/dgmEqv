

import matplotlib.pyplot as plt

# Create a figure and set its size
fig = plt.figure(figsize=(10, 10))

# Add a subplot to the figure
ax = fig.add_subplot(111)

# Data to be plotted
labels = ["18-24", "25-34", "35-44", "45-54", "55-64", "65 and Above"]
sizes = [15, 25, 20, 20, 15, 5]

# Plot the pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Set the title of the graph
ax.set_title('Healthcare Utilization by Age in the USA, 2023')

# Set the font of the title
ax.title.set_fontsize(20)

# Set the font size for the labels
ax.tick_params(axis='both', labelsize=10)

# Set the rotation of the labels
ax.legend(labels, loc="best", bbox_to_anchor=(1.35, 0.8), fontsize='xx-large',
          frameon=False, title='Age')

# Set the length of the labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Automatically resize the image
fig.tight_layout()

# Save the image
plt.savefig(r'pie chart/png/265.png')

# Clear the current image state
plt.clf()