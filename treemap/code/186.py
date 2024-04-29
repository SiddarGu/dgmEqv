import matplotlib.pyplot as plt
import squarify

# Data preparation
data_str = """Social Media,25
Search Engines,20
Streaming Services,15
Online Shopping,15
Email Communication,10
Cloud Services,7
Online Gaming,5
Cybersecurity,3"""

# Splitting the data into labels and values
data_lines = data_str.split('\n')
data_labels = [line.split(',')[0] for line in data_lines]
data = [float(line.split(',')[1]) for line in data_lines]

# Drawing the treemap
plt.figure(figsize=(12, 8))
colors = plt.cm.viridis([0.85, 0.65, 0.45, 0.25, 0.1, 0.2, 0.4, 0.6])
squarify.plot(
    sizes=data,
    label=data_labels,
    color=colors,
    alpha=0.7,
    text_kwargs={'fontsize':10, 'wrap':True}
)

# Adding the title and adjusting layout
plt.title('Percentage Distribution of Internet Usage by Category')
plt.axis('off')
plt.tight_layout()

# Saving the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/186.png"
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current image state
plt.clf()
