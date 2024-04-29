import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Prepare data
data = """Mathematics,50,60,70,80,90,[]
English,45,55,65,75,85,[20,100]
Biology,40,55,70,85,90,[15,95]
Chemistry,48,58,68,78,88,[22,102]
Physics,42,52,62,72,82,[18,98]"""
data = data.split('\n')
subjects = []
box_plot_data = []
outliers = []
for row in data:
    row_data = row.split(',')
    subjects.append(row_data[0])
    box_plot_data.append(list(map(int, row_data[1:6])))
    if row_data[6] != '[]':
        outlier_data = list(map(int, row_data[6][1:-1].split(',')))
        outliers.append(outlier_data)
    else:
        outliers.append([])

# Plotting
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)
ax.boxplot(box_plot_data, whis=1.5)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Add outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

ax.set_xlabel('Subjects')
ax.set_ylabel('Test Scores')
ax.set_title('Test Score Distribution of Students in Different Subjects (2021)')
plt.xticks(np.arange(1, len(subjects) + 1), subjects, rotation='vertical')

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/244_202312310058.png')
plt.clf()
