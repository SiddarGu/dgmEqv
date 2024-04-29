import matplotlib.pyplot as plt
import squarify

# Input data
data_str = """
Department,Workforce Distribution (%)
Operations,25
Sales,20
Human Resources,15
Marketing,15
IT,10
Finance,8
R&D,5
Administration,2
"""
# Process input data
data_lines = data_str.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [float(line.split(',')[1]) for line in data_lines[1:]]

# Create figure
plt.figure(figsize=(12, 8))

# Plot treemap
squarify.plot(sizes=data, label=line_labels, color=None, alpha=0.6)

# Add title and adjust layout
plt.title('Workforce Distribution Across Departments in a Corporate Setting', fontsize=14)
plt.axis('off')
plt.tight_layout()

# Save figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/191.png"
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure state
plt.clf()
