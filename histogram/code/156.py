import matplotlib.pyplot as plt
import numpy as np

# Given data
data_labels = ['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Wind', 'Solar', 'Biomass', 'Geothermal']
data = [1584, 1523, 809, 696, 300, 221, 65, 23]
line_labels = ['Electricity Generation (TWh)']

# Set up the figure and axis
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Create a vertical histogram (bar chart)
bars = ax.bar(data_labels, data, color=plt.cm.Paired(np.arange(len(data))))

# Add grid, title and labels
ax.set_title('Electricity Generation by Energy Source', fontsize=18)
ax.set_xlabel('Energy Source', fontsize=14)
ax.set_ylabel("Electricity Generation (TWh)", fontsize=14)

# Display data labels with rotation if necessary
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", wrap=True)

# Add value labels on the top of the bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords='offset points',
                ha='center', va='bottom')
    
# Adjust layout to make sure content fits properly
plt.tight_layout()

# Save the figure to the specified absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/156.png'
plt.savefig(save_path, bbox_inches='tight')

# Clear the current figure state to prevent memory issues
plt.clf()
