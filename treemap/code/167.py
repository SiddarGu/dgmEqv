import matplotlib.pyplot as plt
import squarify

# Data preparation
data_string = """
Government Branch,Expenditure (%)
Executive,30
Legislative,20
Judicial,15
Defence,20
Education,10
Healthcare,4
Transportation,1
"""
# Parse data
lines = data_string.strip().split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = [float(line.split(",")[1]) for line in lines[1:]]

# Treemap plotting
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.7)

# Title and decorations
plt.title('Government Expenditure Distribution by Branch')
plt.axis('off')

# Make sure the figure attempts to be as clear as possible
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1136.png'
plt.savefig(save_path, format='png')

# Clear the plot state
plt.clf()
