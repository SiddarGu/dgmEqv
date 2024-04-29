import os
import matplotlib.pyplot as plt

data = [
    ["CO2", 10, 50, 100, 150, 200, []],
    ["CH4", 5, 20, 35, 50, 70, [90]],
    ["N2O", 2, 10, 20, 30, 45, [60, 65]],
    ["SO2", 20, 60, 100, 140, 180, [5, 220]],
    ["NOx", 15, 45, 80, 125, 170, [220]],
]
labels = [x[0] for x in data]
data_values = [x[1:-1] for x in data]
outliers = [x[-1] for x in data]

plt.figure(figsize=(10, 7))
ax1 = plt.subplot()
plt.boxplot(data_values, vert=False, labels=labels, whis=1.5)

ax1.set_title('Emission Distribution of Various Pollutants (2021)', fontsize=15)
ax1.set_ylabel('Pollutants', fontsize=12)
ax1.set_xlabel('Emission (Tons)', fontsize=12)

ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax1.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

for i, outlier in enumerate(outliers):
    if outlier:
        ax1.plot(outlier, [i + 1] * len(outlier), 'r.')

plt.tight_layout()
os.makedirs(os.path.dirname('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/'), exist_ok=True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/78_202312270030.png')

plt.clf()
