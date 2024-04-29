import matplotlib.pyplot as plt
import squarify

# Given data transformation
data_labels = ['Hotels', 'Restaurants', 'Travel Agencies', 'Airlines', 'Cruises', 'Tourist Attractions', 'Event Planning']
data = [35, 25, 15, 10, 8, 4, 3]
line_labels = ['Revenue Contribution (%)']

# Drawing the treemap
plt.figure(figsize=(12, 8))
colors = [plt.cm.Spectral(i/float(len(data_labels))) for i in range(len(data_labels))]
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.8, text_kwargs={'fontsize':9, 'wrap': True})
plt.title('Revenue Distribution in the Tourism and Hospitality Industry', fontsize=15)

# Resize the figure before savefig
plt.tight_layout()

# Saving the image to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1007.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state after saving the plot
plt.clf()
