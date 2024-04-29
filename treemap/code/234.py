import matplotlib.pyplot as plt
import squarify

# Data
data_labels = ['Utilities Market Share (%)']
line_labels = ['Coal', 'Natural Gas', 'Nuclear', 'Renewable', 'Oil', 'Hydropower']
data = [25, 30, 15, 20, 8, 2]

# Define color list if you want to specify custom colors
colors = plt.cm.viridis_r([x / max(data) for x in data])

plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7)

plt.title('Utilities Market Share by Energy Source in 2023')

# Ensures that text labels are not overlapping by rotating or wrapping the text
plt.gca().set_xticks([])
plt.gca().set_yticks([])
[plt.text(t.get_position()[0], t.get_position()[1], t.get_text(), ha='center', va='center',
          bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', boxstyle='round,pad=0.1'))
          for t in plt.gca().texts]

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image with an absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/234.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)

# Clear current figure (prevent overlapping of savefigs if you run this block multiple times)
plt.clf()
