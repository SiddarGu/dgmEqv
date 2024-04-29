import matplotlib.pyplot as plt
import squarify

# Given data
raw_data = """
Research Area,Investment Percentage (%)
Artificial Intelligence,25
Renewable Energy,20
Space Exploration,15
Biotechnology,10
Materials Science,10
Robotics,8
Quantum Computing,7
Computer Science,5
"""

# Preparing the data
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Plotting the treemap
fig, ax = plt.subplots(figsize=(12, 8))
cmap = plt.cm.viridis
norm = plt.Normalize(vmin=min(data), vmax=max(data))
colors = [cmap(norm(value)) for value in data]
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, text_kwargs={'fontsize':10, 'wrap':True})
plt.axis('off')
plt.title('Investment Distribution among Key Science and Engineering Research Areas', fontsize=14, y=1.08)

# Save the figure
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/78.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure's state
plt.clf()
