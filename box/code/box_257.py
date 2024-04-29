import matplotlib.pyplot as plt
import numpy as np

# restructure data
law_specialties = ["Family Law", "Criminal Law", "Cyber Law", "Constitutional Law", "Environmental Law"]
dist_data = [
    [40000, 70000, 90000, 115000, 145000], 
    [45000, 77000, 100000, 120000, 150000],
    [50000, 80000, 104000, 128000, 155000],
    [60000, 88000, 110000, 135000, 165000],
    [55000, 83000, 105000, 130000, 160000]
]
outliers = [[160000, 180000], [170000, 190000], [], [180000], [150000, 175000]]

# box plot 
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

# create box plot without outliers
bp = ax.boxplot(dist_data, notch=True, vert=True, patch_artist=True, whis=1.5, showfliers=False)

colors = ['pink', 'lightblue', 'lightgreen', 'pink', 'lightblue']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ko")

ax.set_xticklabels(law_specialties, rotation=45, ha="right", rotation_mode="anchor")
ax.set_xlabel('Law Specialty')
ax.set_ylabel('Salary (USD)')
ax.grid(True)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_title('Salary Distribution in Different Law Specialities 2023')

# save plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/193_202312310058.png')
plt.close()
