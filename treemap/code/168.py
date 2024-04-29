import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Educational Level,Spending (%)
Higher Education,40
Primary and Secondary,35
Early Childhood,12
Adult Education,8
Special Needs Education,5"""

# Process the data
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]  # Getting the label for spending
line_labels = [line.split(',')[0] for line in lines[1:]]  # Getting the educational levels
data = [float(line.split(',')[1]) for line in lines[1:]]  # Getting the spending data as floats

# Plot
fig = plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=.7)

plt.title('Proportional Spending Across Educational Levels', fontsize=18)
plt.axis('off')  # Remove the axes

# Automatically resize the image
plt.tight_layout()

# Save the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/168.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state to prevent re-drawing on the same canvas
plt.clf()
