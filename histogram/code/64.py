import pandas as pd
import matplotlib.pyplot as plt

# Data setup
data_labels = ['Government Spending ($ Billion)']
line_labels = [
    'Healthcare', 'Education', 'Defense', 'Infrastructure',
    'Welfare', 'Environmental Protection', 'Space Exploration',
    'Agriculture', 'Research and Development'
]
data_values = [980, 850, 780, 620, 510, 360, 320, 250, 190]

# Create DataFrame
df = pd.DataFrame(data_values, index=line_labels, columns=data_labels)

# Create figure and add subplot
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plot horizontal histogram
df.plot(kind='barh', legend=False, ax=ax, color=plt.cm.tab20.colors)

# Set title and labels
ax.set_title('Government Spending Allocation by Policy Area (2023)')
ax.set_xlabel('Government Spending ($ Billion)')
ax.set_ylabel('Policy Area')

# Set grid
ax.grid(zorder=0, linestyle='--', linewidth=0.5)

# Rotate the x-axis labels if they are too long
for tick in ax.get_xticklabels():
    tick.set_rotation(45)

# Enable the wrapping of the y-axis labels
ax.set_yticklabels(ax.get_yticklabels(), wrap=True)

# Improve layout
plt.tight_layout()

# Save the figure
output_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/64.png'
plt.savefig(output_path)

# Clear the current image state
plt.clf()
