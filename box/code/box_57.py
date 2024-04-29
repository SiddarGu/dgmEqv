import matplotlib.pyplot as plt

# Manually parsed data from the provided string
conditions = ["Heart Disease", "Diabetes", "Cancer", "Asthma", "Arthritis"]
min_recovery = [30, 20, 40, 10, 35]
q1_recovery = [80, 65, 130, 40, 85]
median_recovery = [120, 115, 180, 70, 125]
q3_recovery = [160, 150, 250, 110, 165]
max_recovery = [230, 200, 300, 140, 200]
outliers = [[], [280], [350, 400], [5, 7, 8], [250]]

# Preparing data for boxplot
box_data = list(zip(min_recovery, q1_recovery, median_recovery, q3_recovery, max_recovery))

# Create the boxplot
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(box_data, notch=True, vert=True, patch_artist=True)

# Customize the boxplot colors
colors = ['pink', 'lightblue', 'lightgreen', 'red', 'purple']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add outliers
for i, outlier in enumerate(outliers):
    if outlier:
        x = [i + 1] * len(outlier)
        ax.plot(x, outlier, 'ro', markersize=5)

# Add grid, labels, and title
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xticklabels(conditions)
ax.set_xlabel('Health Conditions')
ax.set_ylabel('Recovery Time (Days)')
ax.set_title("Patient Recovery Time Distribution for Different Health Conditions (2025)")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/183_202312310058.png')
plt.clf()
