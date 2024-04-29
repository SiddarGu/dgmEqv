import matplotlib.pyplot as plt
import numpy as np

# Data input
data_labels = ['Local Gala', 'Charity Auction', 'Marathon', 'Benefit Concert', 'Online Campaign', 'Bake Sale']
data = [232.5, 310.4, 125.7, 287.3, 345.1, 68.4]
line_labels = ['Amount Raised ($1000)']

# Create figure and add a subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
bars = ax.bar(data_labels, data, color=plt.cm.tab10(np.linspace(0, 1, len(data))))

# Add grid to the background
ax.yaxis.grid(True)

# Wrap labels if too long and rotate them for better fit
plt.xticks(rotation=45, ha='right', wrap=True)

# Add the title
plt.title('Fundraising Performance by Event Type for Nonprofit Organizations')

# Automatically adjust layout to make it fit well within the figure size
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/145.png', format='png')

# Clear current figure state
plt.clf()
