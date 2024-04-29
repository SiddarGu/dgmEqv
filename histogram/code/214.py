import matplotlib.pyplot as plt
import numpy as np

# Given data
data_labels = ['Very Dissatisfied', 'Dissatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']
data = np.array([30, 50, 120, 200, 150])
line_labels = ['Number of Employees']

# Create a figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

# Plotting the histogram
bar_colors = plt.cm.tab10(np.linspace(0, 1, len(data_labels)))
bars = ax.bar(data_labels, data, color=bar_colors, alpha=0.7)

# Adding grid, labels, and title
ax.set_title('Employee Job Satisfaction Levels in the Workplace')
ax.set_xlabel('Job Satisfaction Level')
ax.set_ylabel('Number of Employees')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Handling long text labels
plt.xticks(rotation=45, ha='right', wrap=True)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Annotate each bar with the value
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

# Save the image
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/214.png', format='png', bbox_inches='tight')

# Clear the current image state
plt.clf()
