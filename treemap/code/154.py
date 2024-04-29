import matplotlib.pyplot as plt
import squarify

# Data preparation
data_labels = ['Freight Volume (%)']
line_labels = ['Road', 'Rail', 'Air', 'Sea', 'Pipeline']
data = [40, 20, 15, 20, 5]

# Calculate size of figure for clarity
size = len(line_labels) * 1.5

# Plotting
plt.figure(figsize=(size, size))
squarify.plot(sizes=data, label=line_labels, color=None, alpha=0.8)
plt.title('Freight Volume Distribution by Transportation Mode', fontdict={'fontsize': 20})

# Rotating or wrapping the labels if necessary
for label in plt.gca().texts:
    text = label.get_text()
    if len(text) > 10:
        label.set_text('\n'.join(text.split()))
        label.set_fontsize(9)
        label.set_rotation(30)
    else:
        label.set_fontsize(12)

# Optimize layout and save figure
plt.axis('off')
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/154.png', format='png', dpi=300)
plt.close()
