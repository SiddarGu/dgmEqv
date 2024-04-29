import matplotlib.pyplot as plt

# Data processing based on the information provided
data_labels = ['Number of Concerts']
line_labels = ['<50', '50-100', '100-150', '150-200', '200-250', '250-300', '>300']
data = [34, 58, 45, 38, 28, 19, 8]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting the horizontal histogram
ax.barh(line_labels, data, color=plt.cm.get_cmap('viridis', 7).colors)

# Setting the title of the figure
ax.set_title('Price Distribution for Concert Tickets in the Entertainment Industry')

# Enabling the grid
ax.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Rotate the labels on the x-axis if they are too long
ax.tick_params(axis='x', labelrotation=45)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure to the specified file path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/93.png'
plt.savefig(save_path, format='png')

# Clear the current figure to prevent any overlapping of content
plt.clf()
