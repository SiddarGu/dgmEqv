
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Doctor Visits (Million)', 'Hospital Admissions (Million)', 'Prescription Drugs (Million)', 'Mental Health Visits (Million)']
data = np.array([[120,85,60,45],[140,90,70,50],[145,95,75,55],[155,100,80,60],[160,105,85,65]])
x_values = ['2019', '2020', '2021', '2022', '2023']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, 0, 1.0, 0.8, data[:, i], alpha=0.2 * (i + 1), color=plt.cm.Blues(i/len(y_values)), shade=True)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)
# Rotate the X-axis labels for better readability
ax.view_init(elev=30, azim=30)

ax.set_title("Healthcare Trends - 2019 to 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/8_202312251036.png')
plt.clf()