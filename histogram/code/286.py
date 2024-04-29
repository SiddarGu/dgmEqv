import matplotlib.pyplot as plt
import seaborn as sns

# Data provided:
data = [
    [-10, 0, 4], 
    [0, 10, 12], 
    [10, 20, 20], 
    [20, 30, 15], 
    [30, 40, 9], 
    [40, 50, 5], 
    [50, 60, 2]
]

# Transforming data into three variables as specified:
data_labels = ['Monthly Sales Growth (%)']
line_labels = ['{} to {}'.format(i[0], i[1]) for i in data]
data_values = [i[2] for i in data]

# Create a figure with larger figsize to prevent content from display issues
plt.figure(figsize=(12, 8))

# Add a subplot to the figure
ax = plt.subplot()

# Plot horizontal histogram using Seaborn
sns.barplot(x=data_values, y=line_labels, palette="viridis", orient='h')

# Setting the title of the figure
plt.title('Monthly Sales Growth Percentage Across Retailers', fontsize=16)

# Rotate labels if needed
ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha='right', wrap=True)

# Automatically adjust subplot params for a better fit
plt.tight_layout()

# Save the figure to the specified absolute path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/636.png')

# Clear the current image state at the end of the code to prevent overlap with any future plots
plt.clf()
