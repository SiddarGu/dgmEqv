import matplotlib.pyplot as plt
import squarify

# Given data string, simulating multiline input with .split('/n')
data_str = """Manufacturing Process,Production Efficiency (%)/n
Assembly Line,25/n
Injection Molding,20/n
Casting,15/n
Metal Fabrication,15/n
3D Printing,10/n
Machining,8/n
Stamping,4/n
Extrusion,3"""

# Preparing the data
data_lines = data_str.split('/n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [float(line.split(',')[1]) for line in data_lines[1:]]

# Plotting the treemap
plt.figure(figsize=(12, 6))
squarify.plot(sizes=data, label=line_labels, alpha=0.7)
plt.title('Efficiency Distribution Across Manufacturing Processes', fontsize=16)

# Automatically resize the image and apply tight layout
plt.axis('off')
plt.tight_layout()

# Save the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/182.png'
plt.savefig(save_path)

# Clear the current image state
plt.clf()
