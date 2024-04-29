import matplotlib.pyplot as plt

# Data
data_labels = ['1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10']
data = [18, 15, 12, 9, 7, 6, 4, 3, 2]
line_labels = ["Number of Corporations"]

# Create a figure object and add a subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting the histogram
ax.bar(data_labels, data, color='skyblue', edgecolor='black')

# Adding grid
ax.grid(zorder=0, linestyle='--', color='gray')

# Setting the title
ax.set_title('Analysis of Revenue Ranges Amongst Corporations')

# Labeling the axes
ax.set_xlabel('Revenue Range ($Billion)')
ax.set_ylabel('Number of Corporations')

# Handling long label texts
ax.set_xticklabels(data_labels, rotation=45, ha="right")

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/239.png"
plt.savefig(save_path, format='png')

# Clearing the current figure state
plt.clf()
