import matplotlib.pyplot as plt
import numpy as np

# Given data
data = np.array([22, 34, 58, 85, 76])
data_labels = ['Very Dissatisfied', 'Dissatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']
line_labels = ['Number of Employees']

# Create figure and subplot for histogram
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Plot horizontal histogram
ax.barh(data_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Set title
ax.set_title('Employee Job Satisfaction Levels Across the Organization')

# Add grid
ax.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Handle long text in labels
ax.tick_params(axis='y', labelrotation=30)

# Automatically adjust the size of the figure with tight_layout and save it
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/61.png')

# Clear the current figure's state
plt.clf()
