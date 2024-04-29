import matplotlib.pyplot as plt
import numpy as np

# Define data
data_labels = ['Annual Consumption (terajoules)']
line_labels = ['Fossil Fuels', 'Nuclear', 'Hydropower', 'Wind', 'Solar', 'Geothermal', 'Biomass']
data = np.array([3500.7, 980.5, 1503.3, 1240.8, 995.2, 331.4, 621.6])

# Create figure and subplot
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

# Create histogram
bars = ax.bar(line_labels, data, color=plt.cm.tab20(np.arange(len(data))))

# Add grid
ax.yaxis.grid(True)

# Rotate x-axis labels if too long
plt.xticks(rotation=45, ha='right')

# Add title
plt.title('Annual Energy Consumption by Source')

# Apply tight_layout:
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/21.png')

# Clear the current figure state
plt.clf()
