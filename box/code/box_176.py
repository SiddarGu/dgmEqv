import matplotlib.pyplot as plt

# Define the data
data = [["Marketing", 1, 3, 6, 10, 15, []],
        ["Sales", 2, 5, 10, 14, 18, []],
        ["IT", 3, 7, 11, 15, 20, [25, 30]],
        ["Finance", 2, 6, 10, 13, 16, [19, 22]],
        ["HR", 1, 4, 7, 10, 12, [14,18]]]

# Split the data into two 2D arrays
summary_data = [[x[i] for i in range(1, 6)] for x in data]
outliers = [x[6] for x in data]
categories = [x[0] for x in data]

# Create the figure and plot the boxplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.boxplot(summary_data, whis=1.5)

# Plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'rx')

# Set the title, labels and grid
ax.set_title('Employee Absence Distribution in Different Departments (2021)')
ax.set_ylabel('Absence (Days)')
plt.xticks(rotation=90)
ax.set_xticklabels(categories)
ax.yaxis.grid(True)

# Save and clear the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/199_202312310058.png')
plt.clf()
