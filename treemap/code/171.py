import matplotlib.pyplot as plt
import squarify

# Raw data
raw_data = """Housing Category,Market Share (%)
Single-Family Homes,40
Multi-Family Homes,25
Condominiums,15
Townhouses,10
Manufactured Homes,5
Vacation Homes,3
Co-ops,2"""

# Parse the data
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Treemap plot
plt.figure(figsize=(12, 8))
colors = plt.cm.Paired(range(len(data)))
squarify.plot(sizes=data, label=None, color=colors, alpha=0.8)

# Styling and customization
plt.title("Market Share Distribution in the Real Estate and Housing Market")
plt.axis('off')

# To deal with possibly long labels, you can use the `wrap=True` or custom rotation
for i, patch in enumerate(plt.gca().patches):
    x, y = patch.get_xy()
    width, height = patch.get_width(), patch.get_height()
    if width > height:  # height is not enough for label
        plt.text(x + width/2, y + height/2, line_labels[i], ha='center', wrap=True)
    else:
        plt.text(x + width/2, y + height/2, line_labels[i], ha='center', va='center', rotation=90)

# Adjust the plot
plt.tight_layout()

# Save the figure
output_file = '//cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/171.png'
plt.savefig(output_file, format='png', dpi=300)

# Clear the current figure state
plt.clf()
