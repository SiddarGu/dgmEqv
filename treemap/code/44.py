import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Hotel Accommodation,30
Food Services,25
Travel Agencies,15
Airline Services,10
Tour Operators,7
Cultural Attractions,5
Recreational Activities,4
Transportation Rentals,2
Event Planning,2"""

# Parse data into lists
data_lines = data_str.split('\n')
line_labels = [line.split(',')[0] for line in data_lines]
data = [int(line.split(',')[1]) for line in data_lines]

# Set color palette
colors = plt.cm.tab20c.colors

# Create figure with large size to prevent content from being cut off
fig, ax = plt.subplots(figsize=(12, 8))

# Plot treemap
squarify.plot(sizes=data, label=line_labels, color=colors[:len(data)], alpha=0.7, text_kwargs={'fontsize':9, 'wrap':True})

# Set title and adjust layout
plt.title('Revenue Distribution in the Tourism and Hospitality Industry', fontsize=18)
plt.axis('off')
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/44.png'
plt.savefig(save_path, dpi=300, bbox_inches='tight')

# Clear the figure to release memory
plt.clf()
