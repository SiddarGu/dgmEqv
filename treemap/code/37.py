import matplotlib.pyplot as plt
import squarify

# Given data in a formatted string
data_str = """Tech Sector,Internet Usage (%)
Social Media,25
Online Shopping,20
Streaming Services,18
Cloud Computing,12
Online Education,10
Web Browsing,8
Gaming,4
Email,3"""

# Preprocess the data
data_lines = data_str.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [int(line.split(',')[1]) for line in data_lines[1:]]

# Start plotting
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.8)
plt.title('Internet Usage Breakdown Across Technology Sectors')
plt.axis('off')  # Remove axis

# To prevent content from being displayed improperly, use tight_layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/37.png'
plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')

# Clear the current image state
plt.clf()
