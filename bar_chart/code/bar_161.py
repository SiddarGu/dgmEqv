

import matplotlib.pyplot as plt
import numpy as np

# Set font size
plt.rcParams.update({'font.size': 14})

# Create figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot()

# Create bar chart
data = np.array([[8.4, 7.9], [7.2, 8.2], [7.9, 7.8], [8.3, 8.1]])
x_labels = ['McDonalds', 'KFC', 'Burger King', 'Wendys']
x_pos = np.arange(len(x_labels))

ax.bar(x_pos - 0.2, data[:, 0], width=0.4, label='Customer Rating', color='b')
ax.bar(x_pos + 0.2, data[:, 1], width=0.4, label='Food Taste Rating', color='y')

# Set x-axis labels
ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels, rotation=45, ha='right', wrap=True)

# Set title
ax.set_title('Average Customer and Food Taste Ratings for four fast-food restaurants in 2021')

# Place legend
ax.legend(loc="best")

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/17.png')

# Clear the current image state
plt.clf()