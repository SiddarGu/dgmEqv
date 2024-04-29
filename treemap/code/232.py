import matplotlib.pyplot as plt
import squarify

# Data parsing
data_input = """
Department,Workforce Ratio (%)
Administration,15
Sales,20
Human Resources,10
Research and Development,12
Customer Service,13
IT Support,10
Marketing,10
Production,10
"""

# Splitting the data into lines and then splitting each line into labels and values
lines = data_input.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Creating the figure
plt.figure(figsize=(12, 8))

# Creating a color palette
cmap = plt.cm.viridis
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Plotting the treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7)

# Adding the title
plt.title('Workforce Distribution Across Departments in Corporate Structure', fontsize=18)

# Removing the axes
plt.axis('off')

# Resizing the image to fit content
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/232.png'
plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')

# Clear the current image state
plt.close()
