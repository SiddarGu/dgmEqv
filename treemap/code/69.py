import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Category,Usage Share (%)
Social Media,25
Search Engines,20
Online Shopping,15
Video Streaming,15
Email Services,10
Cloud Computing,5
Cybersecurity,5
Online Gaming,3
Internet of Things,2"""

# Parse the data
lines = data_str.strip().split('\n')
data_labels = lines[0].split(',')[1:]
data = []
line_labels = []

for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append(float(parts[1]))

# Setting color palette
cmap = plt.cm.viridis
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Create a treemap
plt.figure(figsize=(12, 8), dpi=100)
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':10})

# Title and other settings
plt.title('Internet Usage Distribution by Online Activities')
plt.axis('off') # Turn off the axis

# Rescale the figure
plt.tight_layout()

# Save the figure
plt_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/69.png'
plt.savefig(plt_path, bbox_inches='tight')

# Clear the current figure state
plt.clf()
