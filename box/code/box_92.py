import matplotlib.pyplot as plt

# Define the data
data = [['Facebook', 50, 150, 600, 1400, 2500], ['Instagram', 30, 100, 500, 1100, 2300], ['Twitter', 20, 60, 330, 700, 1200], ['LinkedIn', 10, 40, 225, 500, 900], ['Snapchat', 15, 55, 300, 700, 1300]]
outliers = [[], [3000, 3500], [15, 2000], [1000], [1500]]
labels = [row[0] for row in data]

# Create 2D list for boxplot data and remove labels from original 2D list
plot_data = [row[1:] for row in data]

# Create figure
fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot(111)

# Create the boxplot
ax.boxplot(plot_data, whis=1.5, vert=False)

# Plot the outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# Customizing the graph
ax.set_yticklabels(labels)
ax.set_xlabel('User Count (Millions)')
ax.set_title('User Count Distribution in Social Media Platforms (2022)')
plt.grid(True)
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/79_202312270030.png')

# Clear the current figure
plt.clf()
