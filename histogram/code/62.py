import matplotlib.pyplot as plt

# Data provided
data_str = """Product Defect Rate (%),Number of Factories
0-2,48
2-4,35
4-6,27
6-8,15
8-10,5
10-12,4
12-14,2
14-16,1
16-18,1"""

# Transform the data into three variables
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [int(line.split(',')[1]) for line in lines[1:]]

# Create the figure and subplot for horizontal histogram
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(line_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Adding the grid, title, and labels
ax.set_xlabel('Number of Factories')
ax.set_title('Factory Product Defect Rates in the Manufacturing Sector')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Rotate the labels on x-axis if they are too long
plt.xticks(rotation=45, ha='right')
plt.yticks(wrap=True)

# Adjust layout to prevent content from being overlapped
plt.tight_layout()

# Save the figure to the provided path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/62.png', dpi=300)

# Clear the current figure's state to prevent interference with future plots
plt.clf()
