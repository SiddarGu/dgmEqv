import matplotlib.pyplot as plt

# Data
categories = ["Baseball", "Soccer", "Basketball", "Tennis", "Golf"]
values = [[10, 30, 50, 70, 90], [20, 40, 60, 80, 100], [15, 35, 55, 75, 95], [5, 25, 45, 65, 85], [7, 27, 47, 67, 87]]
outliers = [[], [120, 130], [], [0, 5, 95], [0, 3, 107]]

# Create the figure
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Box plot
ax.boxplot(values, whis=1.5)

# Add outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ko")

# Formatting
ax.set_xticklabels(categories, rotation=45)
plt.title("Attendance Distribution at Sports Events in 2021")
plt.ylabel("Attendance (thousands)")
plt.grid(True)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Save the figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/190_202312310058.png")

# Clear the current figure
plt.clf()
