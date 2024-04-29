
import numpy as np
import matplotlib.pyplot as plt

data_labels = ["Q1", "Q2", "Q3", "Q4"]
line_labels = ["Electricity Consumption (kWh)", "Gas Consumption (kWh)", "Renewables Consumption (kWh)", "Nuclear Generation (kWh)", "Fuel Costs (USD)"]
data = np.array([[10,20,30,40],
                 [20,30,40,50],
                 [30,40,50,60],
                 [40,50,60,70],
                 [50,60,70,80]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, np.max(data))
for i in range(len(data)):
    ax.plot(angles, data[i], label=line_labels[i], color=plt.cm.Set1(i))
ax.legend(loc="upper right", bbox_to_anchor=(1.2, 1))
ax.grid(color="grey", linestyle="--", linewidth=1)
plt.title("Energy and Utilities Performance - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/4_202312262300.png")
plt.clf()