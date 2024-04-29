import matplotlib.pyplot as plt

# Data for plotting
data_labels = ['Property', 'Violent', 'Theft', 'Fraud', 'Cyber', 'Drug', 'Public Order', 'Traffic', 'Others']
data = [435, 782, 1234, 556, 239, 860, 312, 687, 165]
line_labels = ['Number of Cases']  # The task specifies no line_labels (no line plot), but the histogram represents this.

# Create figure and axis objects and set a larger figsize
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Create the histogram
bars = ax.bar(data_labels, data, color=plt.cm.Set3.colors, edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Cases')
ax.set_title('Number of Legal Cases by Crime Category')
ax.set_xticklabels(data_labels, rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# Adding a grid
ax.yaxis.grid(True)

# Resize the figure based on the content
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/216.png'
plt.savefig(save_path)

# Clear the current figure state to avoid interference with future plots
plt.clf()
