import matplotlib.pyplot as plt
import squarify

# Given data
raw_data = """
Category,Revenue Share (%)
Team Sports,30
Individual Sports,20
Concerts,15
Movies,20
Streaming Services,10
Video Games,5
"""

# Transforming data into the required variables
data_lines = raw_data.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]  # Column labels
line_labels = [line.split(',')[0] for line in data_lines[1:]]  # Row labels
data = [float(line.split(',')[1]) for line in data_lines[1:]]  # Numerical data

# Visualize the data as a treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.8)
plt.title("Revenue Distribution in Sports and Entertainment Industry")
plt.axis('off')  # Disable the axis lines and labels

# Enforce tight layout to avoid clipping of labels and save the figure
plt.tight_layout()

# Saving the image to the specified absolute path
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/27.png"
plt.savefig(save_path, dpi=100, bbox_inches='tight')  # Set high dpi for clear text

# Clear the current figure to prevent overlap if more plots are created later
plt.clf()
