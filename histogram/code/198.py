import matplotlib.pyplot as plt

# Given data
data_labels = ['Revenue Range ($Million)', 'Number of Companies']
line_labels = [
    '0-50', '50-100', '100-150', '150-200', '200-250',
    '250-300', '300-350', '350-400', '400-450', '450-500'
]
data = [18, 22, 30, 25, 19, 11, 8, 5, 3, 2]

# Create figure and subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plot horizontal bar chart
ax.barh(line_labels, data, color='skyblue', edgecolor='black')

# Add grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Set title
plt.title('Financial Performance of Companies in the Sports and Entertainment Industry')

# Label rotation and wrapping in case of long text
ax.tick_params(axis='y', labelrotation=45)
plt.xticks(wrap=True)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/198.png'
plt.savefig(save_path, format='png')

# Clear the current figure
plt.clf()
