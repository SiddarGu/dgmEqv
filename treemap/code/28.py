import matplotlib.pyplot as plt
import squarify

# Data from the provided string
data_str = """Social Media,25
Search Engines,20
Online Shopping,15
Email Communications,15
Video Streaming,12
Online Gaming,7
Cloud Services,4
Cybersecurity,2"""

# Split string into lines and then split each line into label and value
lines = data_str.split('\n')
data_labels = [line.split(',')[0] for line in lines]
data = [float(line.split(',')[1]) for line in lines]

# Define colors for each section
colors = plt.cm.Spectral([0.1 + 0.8 * (i / len(data_labels)) for i in range(len(data_labels))])

# Plotting the figure with the squarify plot
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':10, 'wrap':True})
plt.title('Internet Usage Distribution by Online Activities', fontsize=18)

# Remove the axes
plt.axis('off')

# Auto-resize the plot and ensure the labels fit well
plt.tight_layout()

# Define the image save path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/28.png'

# Save the figure
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure's state
plt.clf()
