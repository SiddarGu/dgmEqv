import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Training Hours (%)']
line_labels = ['IT', 'Sales', 'Marketing', 'Human Resources', 'Operations', 'Customer Service', 'Research & Development']
data = [18, 22, 20, 15, 10, 8, 7]

# Define colors for different treemap parts, you can use any other colors
colors = plt.cm.tab10.colors

# Plotting - figsize set to a larger value to accommodate labels
fig, ax = plt.subplots(figsize=(12, 8))

# Create a treemap with labels and data
squarify.plot(sizes=data, label=line_labels, color=colors[:len(data)], alpha=.8, text_kwargs={'wrap': True})

# Add title
plt.title('Allocation of Employee Training Hours by Department')

# Resize plot to fit content and avoid clipping
plt.tight_layout()

# Save the figure to the specified file path
file_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/10.png'
plt.savefig(file_path, format='png', dpi=300)

# Clear the current figure to avoid overlapping of figures when plotted multiple times
plt.clf()
