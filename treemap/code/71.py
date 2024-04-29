import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Consumer Electronics,22
Automobiles,18
Pharmaceuticals,15
Aerospace,13
Food and Beverage,12
Machinery,10
Textiles,5
Chemicals,3
Metal Fabrication,2"""

# Processing the data
lines = data_str.split("\n")
data_labels = [line.split(",")[0] for line in lines]
data = [float(line.split(",")[1]) for line in lines]

# Treemap plot
plt.figure(figsize=(12, 8))
colors = plt.cm.viridis(range(len(data_labels)))
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.8)

# Styling and layout adjustments
plt.title("National Manufacturing Production Share by Sector", fontsize=18)
plt.axis('off')
plt.tight_layout()

# Save figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/71.png"
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure's state to prevent interference with future plots
plt.clf()
