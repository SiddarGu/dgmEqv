import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
data_labels = ['Active Users (Millions)', 'Social Platform']
line_labels = ['Facebook', 'YouTube', 'WhatsApp', 'Instagram', 'WeChat', 'TikTok', 'Snapchat', 'Twitter', 'Reddit', 'LinkedIn']
data = [2580, 2291, 2000, 1500, 1254, 1000, 514, 397, 330, 310]

# Create a figure
fig, ax = plt.subplots(figsize=(14, 10))

# Plotting the horizontal histogram
bar_colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(data))) # Using a color map for fancier colors
bars = ax.barh(line_labels, data, color=bar_colors, edgecolor='gray')

# Adding grid
ax.set_axisbelow(True)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Set the title
plt.title('Active User Distribution Across Major Social Media Platforms')

# Adding the data labels
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 50  # leaving a little offset from the right end of the bar
    plt.text(label_x_pos, bar.get_y() + bar.get_height()/2, str(width), va='center')

# Handling long label texts
plt.yticks(rotation=45, ha='right')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/70.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
