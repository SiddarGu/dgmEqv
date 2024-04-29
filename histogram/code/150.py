import matplotlib.pyplot as plt

# Prepare the data
data_labels = ['Defense', 'Education', 'Healthcare', 'Social Security', 'Infrastructure', 
               'Research and Development', 'Environmental Protection', 'International Aid', 
               'Energy', 'Agriculture']
data = [732, 620, 868, 1105, 136, 160, 69, 51, 96, 132]

# Create a new figure with a specified figure size
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot a horizontal bar chart
ax.barh(data_labels, data, color=plt.cm.viridis_r(range(len(data_labels))))

# Set the grid, title, and labels
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_title('Allocation of Federal Budget Across Different Policy Areas')
ax.set_xlabel('Annual Budget (Billion USD)')

# Rotate the y-axis labels if they are too long
ax.tick_params(axis='y', labelrotation=45)

# Make sure all text labels and content fit well
plt.tight_layout()

# Finally, save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/150.png')

# Clear the current figure to prevent overlapping of images if this code is run multiple times
plt.clf()
