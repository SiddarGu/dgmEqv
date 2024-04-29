import matplotlib.pyplot as plt
import os

# Given data formatted for clarity and proper variable assignment
data_labels = ['Facebook', 'YouTube', 'WhatsApp', 'Instagram', 'WeChat', 'TikTok', 'Reddit', 'Twitter', 'LinkedIn', 'Snapchat']
data = [2600, 2291, 2000, 1500, 1258, 1000, 430, 396, 310, 306]
line_labels = 'Monthly Active Users (Millions)'

# Create a figure and a histogram
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)

# Plotting the histogram
ax.bar(data_labels, data, color='skyblue')

# Adding grid, title, and labels
plt.title('Monthly Active User Comparison Among Major Social Media Platforms')
plt.xlabel('Social Media Platform')
plt.ylabel(line_labels)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Setting the rotation of the x-tick labels
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Check directory and save the image to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/243.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure state to avoid memory issues
plt.clf()
