

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# data 
subjects = ['Math', 'Physics', 'English', 'History', 'Chemistry']
Min = [50, 40, 45, 30, 35]
Q1 = [70, 60, 65, 55, 60]
Median = [80, 75, 75, 70, 70]
Q3 = [90, 85, 85, 80, 80]
Max = [100, 95, 95, 90, 95]
Outlier = [[], [110], [0, 105], [95, 105], [105]]

# figure
plt.figure(figsize=(10,6))

# boxplot
ax = plt.subplot()
ax.boxplot(np.array([Min, Q1, Median, Q3, Max]), labels=subjects, sym='', meanline=True, showmeans=True)

# outlier
for i, outlier in enumerate(Outlier):
    for o in outlier:
        ax.scatter(i + 1, o, marker='x', color='red', s=50)

# title
ax.set_title("Academic Performance Distribution of Students in 2021", fontsize=16, pad=20)

# grid
ax.grid(axis='y', linestyle='--', linewidth=1, color='grey', alpha=0.6)

# tight layout
plt.tight_layout()

# savefig
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/5.png', dpi=150)

# clear figure
plt.clf()