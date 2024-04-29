import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Budget Allocation (%)']
line_labels = ['Executive', 'Legislative', 'Judicial', 'Defense & Military', 'Education', 
               'Healthcare', 'Social Security', 'Environment', 'Transportation']
data = [35, 12, 8, 15, 10, 10, 5, 3, 2]

# Set up the figure size
plt.figure(figsize=(12, 8))

# Create a treemap with colors
colors = plt.cm.viridis(range(len(line_labels)))

# Use squarify to plot the treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, text_kwargs={'wrap': True})

# Set the title of the treemap
plt.title('Percentage Distribution of Public Policy Budget by Government Branches')

# Remove the axis
plt.axis('off')

# Layout optimization 
plt.tight_layout()

# Save the figure
output_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/151.png'
plt.savefig(output_path, format='png', dpi=300)

# Clear the current figure state to avoid overlap if the script runs again
plt.clf()
