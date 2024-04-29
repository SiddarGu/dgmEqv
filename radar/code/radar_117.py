import numpy as np
import matplotlib.pyplot as plt

data = np.array([[75, 80, 70, 68, 82, 85],
                 [80, 85, 85, 75, 75, 80],
                 [90, 85, 95, 80, 75, 90],
                 [75, 80, 85, 65, 95, 70],
                 [70, 65, 60, 65, 90, 75],
                 [80, 85, 90, 70, 95, 85]])

data_labels = ['Abstract Art', 'Impressionism', 'Renaissance Art', 'Cubism', 'Pop Art', 'Surrealism']
line_labels = ['Public Interest (Score)', 'Cultural Impact (Score)', 'Artistic Value (Score)', 'Contemporary Relevance (Score)', 'Popularity among Youth (Score)', 'Market Value (Score)']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(data.shape[0]):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

ax.set_rmax(np.max(data))
ax.legend(line_labels)

plt.title('Radar Analysis of Different Art Movements')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/190_202312310100.png')
plt.close()