import matplotlib.pyplot as plt
import numpy as np

# Data provided
data_str = """
Age Group (Years),Average Daily Time on Social Media (minutes)
13-17,130
18-24,107
25-34,93
35-44,74
45-54,60
55-64,47
65+,30
"""

# Transforming the data into the desired format
data_lines = data_str.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]  # Column labels
line_labels = [line.split(',')[0] for line in data_lines[1:]]  # Row labels
data = [int(line.split(',')[1]) for line in data_lines[1:]]  # Data values

# Visualization using matplotlib
plt.figure(figsize=(10, 7))
ax = plt.subplot()

# Create a horizontal bar chart
ax.barh(line_labels, data, color=plt.cm.viridis(np.linspace(0.3, 0.7, len(data))))

# Adding the grid, title and labels
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.set_title('Average Daily Time Spent on Social Media by Age Group')
ax.set_xlabel('Average Daily Time (minutes)')

# Managing long label texts to prevent overlapping
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/39.png')

# Clear the current figure state to prevent reuse
plt.clf()
