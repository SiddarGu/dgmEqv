import matplotlib.pyplot as plt
import squarify

# Data preparation
data_labels = ["Logistics Volume (%)"]
line_labels = ["Road Freight", "Ocean Shipping", "Rail Transport", "Air Freight", "Pipeline", "Intermodal"]
data = [35, 25, 20, 10, 5, 5]

# Plotting treemap
plt.figure(figsize=(12, 8)) 
squarify.plot(sizes=data, label=line_labels, alpha=.8)

# Title and styling
plt.title('Distribution of Logistics Volume by Transportation Type')
plt.axis('off')

# Automatically resize the image
plt.tight_layout()

# Create the directory if it does not exist
import os
directory = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the figure
plt.savefig(f'{directory}/1046.png', format='png', dpi=300)

# Clear the current figure state to avoid interference with future plots
plt.clf()
