
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10, 6))

# Create subplot
ax = plt.subplot()

# Set x axis data
x_data = ('January', 'February', 'March', 'April')

# Set y axis data
y_data = np.array([[100, 90, 110, 120],
                   [130, 100, 95, 125],
                   [90, 105, 115, 90],
                   [90, 115, 130, 125]])

# Set different color for each line
colors = ('C0', 'C1', 'C2', 'C3')

# Draw line chart
for i in range(len(y_data)):
    ax.plot(x_data, y_data[i], label='Production %s' % chr(65+i), color=colors[i])

# Set title
ax.set_title('Production of four types of goods in the first four months of 2021')

# Set x axis label
ax.set_xlabel('Month')

# Set y axis label
ax.set_ylabel('Units')

# Add legend
ax.legend(loc='best')

# Set grid
ax.grid(True)

# Set x axis ticks
ax.set_xticks(x_data)

# Rotate x axis ticks
plt.xticks(rotation=45)

# Add labels to each data point
for x, y_list in zip(x_data, y_data):
    for i in range(len(y_list)):
        ax.annotate(y_list[i], xy=(x, y_list[i]), xytext=(0, 5), 
                    textcoords='offset points', rotation=45,
                    wrap=True, color=colors[i])

# Automatically adjust image size
plt.tight_layout()

# Save image
plt.savefig('line chart/png/344.png')

# Clear image state
plt.clf()