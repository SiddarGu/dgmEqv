import matplotlib.pyplot as plt

# Data preparation
data_labels = ["Average Test Score"]
line_labels = ["Kindergarten", "Elementary", "Middle School", "High School", "Undergraduate", "Postgraduate"]
data = [82.5, 88.7, 85.3, 79.8, 73.4, 81.2]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Create a vertical histogram
ax.bar(line_labels, data, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])

# Add grid, title, and labels
ax.set_title('Average Test Scores by Educational Grade Level', fontsize=15)
ax.set_ylabel('Scores', fontsize=12)
for label in ax.get_xticklabels():
    label.set_rotation(45)
    label.set_wrap(True)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust subplot params for a clear layout
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/33.png', format='png')

# Clear the current figure state at the end of the code to avoid any overlaps
plt.clf()
