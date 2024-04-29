import matplotlib.pyplot as plt

# Restructure the data
subjects = ["Sociology", "Psychology", "Philosophy", "History", "Cultural Studies"]
box_plot_data = [[50, 150, 300, 450, 600], [75, 200, 350, 500, 650], [30, 100, 200, 300, 400], [45, 135, 225, 315, 405], [60, 180, 300, 420, 540]]
outliers = [[], [25,700], [15,450], [10,450], [20,600]]

# Create the figure and axis
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Create the box plot
bp = ax.boxplot(box_plot_data, vert=0, patch_artist=True, notch=True, whis=1.5)

colors = ['cyan', 'lightblue', 'lightgreen', 'tan', 'pink']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

ax.set_title('Citation Distribution in Social Sciences & Humanities Subjects (2021)')
ax.set_yticklabels(subjects)
ax.set_xlabel('Citation (Count)')
plt.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/104_202312270030.png')

# Clear the current figure
plt.close(fig)
