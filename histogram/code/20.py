import matplotlib.pyplot as plt
import os

# Data
data_labels = ['Electronics', 'Automobiles', 'Furniture', 'Textiles', 'Pharmaceuticals', 'Plastics', 'Beverages']
data = [320, 210, 150, 190, 120, 80, 145]
line_labels = ['Units Produced (Thousands)']  # Assuming there's only one data line

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
bars = ax.bar(data_labels, data, color=plt.cm.tab20.colors)

# Adding grid, labels, and title
ax.set_xlabel('Product Type')
ax.set_ylabel('Units Produced (Thousands)')
ax.set_title('Annual Production Volume by Manufacturing Sector')
ax.grid(True, linestyle='--', which='both', axis='y', alpha=0.7)

# Set the rotation of the x labels. If the labels are too long, they will be wrapped automatically.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", wrap=True)

# Adding the data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom')  # Add the data label inside bar

# Optional style
plt.tight_layout()

# Generate the full directory if not exists
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Save the figure
file_path = os.path.join(save_dir, '20.png')
plt.savefig(file_path, format='png', dpi=300)

# Clear the current figure state to avoid state corruption on subsequent plots
plt.clf()
