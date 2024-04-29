import matplotlib.pyplot as plt

# Data
categories = ["Surgery", "Checkup", "Therapy", "Dental Visit", "Vaccination"]
data = [[10, 20, 30, 40, 50], [1, 5, 10, 15, 20], [2, 10, 20, 30, 40], [1, 3, 7, 10, 15], [0, 1, 3, 5, 7]]
outliers = [[], [25], [45, 50], [0.5, 20], [10]]

# Plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Box plot
ax.boxplot(data, whis=1.5)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ko")

# Format axes
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)
ax.set_axisbelow(True)
ax.set_title('Wait Time Distribution for Healthcare Procedures (2022)')
ax.set_xlabel('Healthcare Procedure')
ax.set_ylabel('Wait Time (Days)')
plt.xticks(range(1, len(categories) + 1), categories, rotation=45, ha='right')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/81_202312270030.png')

# Clear the figure
plt.clf()
