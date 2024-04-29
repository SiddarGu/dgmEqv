import matplotlib.pyplot as plt

# Data from the assignment
raw_data = """
Daily Sales ($Thousand),Number of Restaurants
0-2,12
2-4,18
4-6,30
6-8,25
8-10,22
10-12,15
12-14,9
14-16,6
16-18,3
18-20,2
"""

# Process raw data
lines = raw_data.strip().split('\n')

# Extract column labels and row labels
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]

# Extract numeric data
data = [int(line.split(',')[1]) for line in lines[1:]]

# Create the figure and axes
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plot the horizontal bar chart
ax.barh(line_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Set the title
ax.set_title('Daily Sales Range for Restaurants in the Food and Beverage Industry')

# Add grid lines and labels
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_xlabel('Number of Restaurants')

# Handle long text in labels
ax.set_yticklabels(line_labels, rotation=0, wrap=True)

# Automate spacing to account for long labels and prevent content from being cropped
plt.tight_layout()

# Save the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/26.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
