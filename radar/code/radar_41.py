
import numpy as np 
import matplotlib.pyplot as plt 

data_labels = ['2020','2021','2022','2023','2024','2025']
line_labels = ['Carbon Emission (kg/capita)','Renewable Energy Sources (%)','Water Consumption (m3/capita)','Recycling Rate (%)','Air Quality (AQI)']
data = np.array([[14.65,14.5,14.3,14.1,13.9,13.7],[20,25,30,35,40,45],[90,85,80,75,70,65],[50,55,60,65,70,75],[130,125,120,115,110,105]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels)+1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12)
ax.set_rlim(0, np.max(data))
for i in range(data.shape[0]):
    ax.plot(angles, data[i], 'o-', label=line_labels[i], color=plt.cm.Set1(i)) 
plt.title('Progress of Sustainability in Next 5 Years')
plt.legend(bbox_to_anchor=(1.2,1.1))
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/1_202312262320.png")
plt.clf()