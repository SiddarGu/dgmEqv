import matplotlib.pyplot as plt
import os

# Data processing
data_labels, line_labels, data = ['Monthly Sales (Million USD)', 'Number of Retailers'], \
                                 ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                                  'August', 'September', 'October', 'November', 'December'], \
                                 [(45, 38, 50, 55, 60, 53, 65, 70, 62, 56, 80, 90)]

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Plot vertical histogram
ax.bar(line_labels, data[0], color=plt.cm.viridis(np.linspace(0, 1, len(data[0]))))

# Title and labels
ax.set_title('Monthly Sales Distribution Among Retailers in E-commerce Sector', fontsize=15)
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)

# Add grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate the x-axis labels if they are too long
plt.xticks(rotation=45, ha='right')

# Adjust the layout
plt.tight_layout()

# Create necessary paths
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/168.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Saving the figure
plt.savefig(save_path)

# Clear the current figure's state to start fresh for new plots
plt.clf()
