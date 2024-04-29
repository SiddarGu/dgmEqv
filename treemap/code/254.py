import matplotlib.pyplot as plt
import squarify

# Parsing the provided data
data_raw = """Social Media,25
Search Engines,20
Streaming Services,18
Online Shopping,15
Cloud Computing,10
Online Gaming,7
Email Services,3
Cybersecurity,2"""

# Extracting data
data_labels = ["Usage Share (%)"]
line_labels = []
data = []

# Split data into lines and then extract label and value
for line in data_raw.split('\n'):
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append(float(parts[1]))

# Draw the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.7)
plt.title('Internet Usage Distribution Across Different Services in 2023', fontsize=18)
plt.axis('off')  # Disable the axis

# Tight layout to prevent content from being cut off
plt.tight_layout()

# Ensure directory exists before saving
import os
dir_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(dir_path, exist_ok=True)

# Save the figure
plt.savefig(f"{dir_path}/1031.png", bbox_inches='tight', dpi=300)

# Clear the current figure state
plt.clf()
