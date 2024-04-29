
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Hotels', 'Restaurants', 'Tourist Attractions', 'Tour Companies', 'Travel Agents', 'Airports', 'Transportation Services', 'Entertainment Venues', 'Cultural Events']
line_labels = ['Category', 'Number']
data = [500, 400, 300, 250, 200, 150, 100, 50, 25]

# Create figure and set up the axes
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

# Calculate the sector angle
sector_angle = (2 * np.pi) / len(data_labels)

# Plot the data using the rose chart
for i, v in enumerate(data):
    ax.bar(i * sector_angle, v, width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

# Add a legend
ax.legend(data_labels, bbox_to_anchor=(1.1, 1.05))

# Set the number of ticks to match the number of categories
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))

# Set the ticks to the labels
ax.set_xticklabels(data_labels, wrap=True, fontsize=10, color='black')
ax.tick_params(axis='x', pad=15)

# Set the title
ax.set_title('Number of Tourism and Hospitality Services in 2021', pad=25, fontsize=15, color='black')

# Adjust the layout to prevent content from being displayed
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_56.png')

# Clear the current image state
plt.clf()