import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Platform Category,User Engagement (%)
Social Networking,35
Search Engines,25
Online Shopping,15
Video Streaming,10
Blogging Platforms,5
Email Services,5
Online Gaming,3
News Websites,2"""

# Transforming data
lines = data_str.split("\n")
data_labels = lines[0].split(",")[1:]  # Extracting column labels
line_labels = [line.split(",")[0] for line in lines[1:]]  # Extracting row labels
data = [float(line.split(",")[1]) for line in lines[1:]]  # Extracting numerical data

# Plot Treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=.8)

# Title and other customizations
plt.title('User Engagement Across Web Platforms in Social Media Era')
plt.axis('off')

# Automatic resizing of the image to prevent content overflow
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1122.png'
plt.savefig(save_path, format='png')

# Clear current figure state after saving the image
plt.clf()
