import numpy as np
import matplotlib.pyplot as plt

data = np.array([[90, 85, 70, 80, 75],
                 [80, 85, 90, 95, 90],
                 [70, 75, 80, 85, 80],
                 [85, 90, 95, 80, 75],
                 [80, 85, 90, 85, 80]])

data_labels = ["Basketball", "Football", "Tennis", "Golf", "Rugby"]
line_labels = ["Audience Engagement (%)", "Player Performance (Score)", "Event Quality (Score)", "Ticket Sales (%)", "Brand Recognition (%)"]

# Append the first element of each row to the end for close-loop plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], linewidth=2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.amax(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

legend_handles, legend_labels = ax.get_legend_handles_labels()
ax.legend(legend_handles, line_labels, loc='upper right')

plt.title("Sports and Entertainment Performance Evaluation")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/76_202312302350.png")
plt.clf()