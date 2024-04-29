import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Define the data
data_labels = ['Annual Budget (Billion $)']
line_labels = ['National Defense', 'Education', 'Infrastructure', 'Health Care', 
               'Environmental Protection', 'Social Security', 'Research and Development', 
               'Foreign Aid', 'Public Safety']
data = [721, 102, 96, 150, 82, 910, 138, 27.5, 63]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create figure and axes
plt.figure(figsize=(12, 8))
ax = plt.subplot(111)

# Plot the data
df.plot(kind='bar', ax=ax, rot=0, grid=True, legend=False)

# Set the title
ax.set_title('Allocation of Government Budget by Policy Area', fontsize=16)

# Set x-axis label
ax.set_xlabel('Policy Area', fontsize=14)

# Set y-axis label
ax.set_ylabel('Annual Budget (Billion $)', fontsize=14)

# Enable the grid
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Rotate the x-axis labels if needed
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    tick.set_horizontalalignment('right')

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/237.png')

# Clear the current figure state
plt.close()
