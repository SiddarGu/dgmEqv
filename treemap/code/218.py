import matplotlib.pyplot as plt
import squarify

# Data preparation
data_labels = ['Solar', 'Wind', 'Hydroelectric', 'Natural Gas', 'Coal', 'Nuclear', 'Biomass', 'Geothermal']
data = [22, 20, 18, 15, 10, 8, 4, 3]
colors = plt.cm.viridis(range(len(data)))
line_labels = ['Utility Output (%)']

# Plotting the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':10, 'wrap':True})
plt.title('Energy Production Breakdown by Source', fontsize=16)

# Improve the plot layout to ensure labels and title are not cut-off
plt.tight_layout()

# Saving the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/218.png', format='png', dpi=300)

# Clear the current figure state to avoid interference with other plots
plt.clf()
