import matplotlib.pyplot as plt

# Data processing
data_labels = ['Hours Spent Daily', 'User Count (Millions)']
line_labels = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10']
data = [55, 80, 120, 140, 90, 60, 30, 20, 10, 5]

# Initialize the figure and axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

# Create the histogram
ax.bar(line_labels, data, color='skyblue', edgecolor='black')

# Adding grid, labels, and title
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xlabel(data_labels[0], labelpad=15, size=12)
ax.set_ylabel(data_labels[1], labelpad=15, size=12)
ax.set_title('Daily Social Media Usage Patterns', pad=20, size=16)
ax.tick_params(axis='x', rotation=45)  # To prevent labels from overlapping

# Automatically adjust subplot params for the figure
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/55.png'
plt.savefig(save_path, format='png', dpi=300)  # dpi for high resolution

# Clear the current figure state after saving
plt.clf()
