
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Solar","Wind","Hydro","Natural Gas"]
line_labels = ["Efficiency (%)","Reliability (Score)","Cost (Dollars/MWh)","Carbon Emission (g/MWh)","Availability (Hours)"]
data = np.array([[90,95,85,80],[95,90,85,80],[50,60,70,80],[200,150,100,50],[20,25,30,35]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True) 
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

ax.plot(angles, data[0], 'o-', label= line_labels[0], color='red')
ax.plot(angles, data[1], 'o-', label= line_labels[1], color='green')
ax.plot(angles, data[2], 'o-', label= line_labels[2], color='blue')
ax.plot(angles, data[3], 'o-', label= line_labels[3], color='orange')
ax.plot(angles, data[4], 'o-', label= line_labels[4], color='purple')

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=20, rotation='vertical')
ax.set_rlim([0,200])
ax.set_title("Energy and Utilities - 2021 Performance Overview", fontsize=20)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9,0.95))

ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/1_202312262300.png')
plt.clf()