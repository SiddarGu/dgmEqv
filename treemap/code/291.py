import matplotlib.pyplot as plt
import squarify

# Data extraction
data_str = 'Accommodation,30\nFood and Beverage,20\nTour Operators,15\nAirlines,15\nCruise Lines,10\nRecreation,5\nTransportation Services,3\nTravel Agencies,2'
pairs = [x.split(',') for x in data_str.split('\n')]
line_labels, data = zip(*pairs)  # This will create two tuples: one for line labels and the other for data
data = [float(value) for value in data]  # Convert data to floats

# Visualization
plt.figure(figsize=(12, 8))
# Create a color palette
cmap = plt.cm.coolwarm
mini=min(data)
maxi=max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Creating the treemap
squarify.plot(sizes=data, label=line_labels, color=colors, pad=True, text_kwargs={'wrap': True})

plt.title('Revenue Distribution in the Tourism and Hospitality Industry')
plt.axis('off')
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/291.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)

# Clear the current figure state after saving the image
plt.clf()