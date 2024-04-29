import matplotlib.pyplot as plt
import os

# Given structured data
data_labels = ["Facebook", "YouTube", "WhatsApp", "Instagram", "WeChat", "TikTok", "Snapchat", "Twitter"]
line_labels = ["Daily Active Users (Millions)"]
data = [210, 192, 166, 122, 89, 76, 68, 55]

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Plot histogram
ax.bar(data_labels, data, color='skyblue')

# Set title
ax.set_title('Daily Active User Counts Across Various Social Media Platforms')

# Add grid
ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Rotate x-axis labels if too long
plt.xticks(rotation=45, ha='right')

# Before saving figure, automatically resize the image and add padding to fit all elements
plt.tight_layout()

# Check if the save path exists, if not create the path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Save the plot as an image file
plt.savefig(f"{save_path}/633.png", format='png', dpi=300)

# Clear the current image state
plt.clf()
