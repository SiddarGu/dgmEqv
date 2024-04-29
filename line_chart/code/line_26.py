
import matplotlib.pyplot as plt
import numpy as np

# Set up figure
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 1, 1)

# Create data
x_data = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July'])
y_data = np.array([100, 110, 105, 115, 120, 125, 130])

# Plot line chart
ax.plot(x_data, y_data, marker='o', linestyle='-', color='c', linewidth=2.5)

# Set x-axis
ax.set_xticks(np.arange(len(x_data)), minor=False)
ax.set_xticklabels(x_data, rotation=45, ha='right')
plt.xticks(rotation=45, ha='right')

# Set y-axis
ax.set_ylim(0, 140)
plt.yticks(np.arange(0, 140, 10))

# Set title and labels
ax.set_title('Number of Social Media Users from January to July 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Users')

# Show legend 
ax.legend(loc='upper right')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/44.png')

# Clear the current image state
plt.cla()