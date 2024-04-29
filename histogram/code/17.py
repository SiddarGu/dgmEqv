import matplotlib.pyplot as plt
import os

# Data Preparation
data_labels = ['200-400', '400-600', '600-800', '800-1000', '1000-1200', 
               '1200-1400', '1400-1600', '1600-1800', '1800-2000']
data = [45, 55, 35, 40, 25, 15, 10, 5, 3]
line_labels = ['Average House Price ($\'000)', 'Number of Transactions']

# Create a figure and a horizontal bar chart
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Create horizontal bar chart
bars = ax.barh(data_labels, data, color=plt.cm.Set3(range(len(data))), edgecolor='gray')

# Adding the grid
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Add Title
plt.title('Real Estate Transactions Distribution by House Price Range')

# Set label if too long
ax.set_yticklabels(data_labels, rotation=45, ha='right', wrap=True)

# Automatically resize the image
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/17.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='png')

# Clear the current figure's state
plt.clf()
