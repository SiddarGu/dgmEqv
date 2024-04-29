
import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

# Define labels 
x_labels = ["New York", "Los Angeles", "San Francisco", "Chicago"]
y_labels_price = [600000, 450000, 700000, 400000]
y_labels_rent = [3500, 2500, 3000, 2000]

# Define bar width and bar positions
bar_width = 0.3
ind = np.arange(len(y_labels_price))

# Create the bars
ax.bar(ind, y_labels_price, width=bar_width, label="Average Home Prices (USD)")
ax.bar(ind + bar_width, y_labels_rent, width=bar_width, label="Average Rent (USD)")

# Set x-axis and y-axis limits
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(0, 800000)

# Set x labels
ax.set_xticks(ind + bar_width / 2)
ax.set_xticklabels(x_labels, rotation=45, wrap=True)

# Add legend and title
ax.legend(loc='upper right')
plt.title("Average Home Prices and Rents in four major cities in 2021")

# Adjust image size and save
plt.tight_layout()
plt.savefig("bar chart/png/436.png")

# Clear the current image state
plt.clf()