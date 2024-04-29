import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ["Usage Share (%)"]
line_labels = ["Social Media", "Online Shopping", "Streaming Services", "Gaming",
               "Online News", "Cloud Services", "Remote Work", "E-Learning"]
data = [25, 18, 17, 16, 9, 8, 4, 3]

# Creating a figure with a specific size to ensure it's big enough
plt.figure(figsize=(12, 8))

# Treemap plot using squarify
colors = plt.cm.viridis(range(0, 256, int(256/len(data))))
squarify.plot(sizes=data, label=line_labels, alpha=0.8, color=colors)

# Adding title, formatting it, and styling the labels
plt.title("Online Usage Distribution Across Internet Activities in 2023", fontsize=14, weight='bold')
plt.axis('off')

# Resizing layout and saving the figure
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1117.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
