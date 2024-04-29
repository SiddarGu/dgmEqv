import matplotlib.pyplot as plt

# Data preparation
data_labels = ['Percentage of Population']
line_labels = ['Less than High School', 'High School Graduate', 'Some College', 
               "Bachelor's Degree", 'Postgraduate Degree', 'Doctorate']
data = [12.5, 25.8, 20.3, 18.4, 15.6, 7.4]

# Create a new figure with given figsize
plt.figure(figsize=(10, 8))

# Add subplot
ax = plt.subplot()

# Create a horizontal bar chart
ax.barh(line_labels, data, color=plt.cm.tab10(range(len(data))), edgecolor='black')

# Add grid with zorder to put the grid below the bars
ax.grid(which='major', linestyle='--', linewidth='0.5', color='grey', zorder=0)

# Set title of the chart
ax.set_title('Education Attainment Levels in the Adult Population')

# Handle long text of the labels with rotation or wrap
ax.xaxis.set_tick_params(rotation=45)
ax.set_xticklabels(ax.get_xticklabels(), wrap=True)
ax.set_xlabel('Percentage of Population')

# Handle long text labels to avoid stacking or overwriting
ax.tick_params(axis='y', labelsize=10)

# Automatically adjust subplot params for a nice fit
plt.tight_layout()

# Save the figure to the specified path with a high dpi for clarity
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/41.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure's state
plt.clf()
