
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Local Taxes","Public Transport","Education","Public Safety","Social Services","Infrastructure","Environmental Protection","Healthcare"]
data = [30,20,10,40,50,25,15,60]
line_labels = ["Topic","Number"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')
sector_angle = (2 * np.pi) / len(data_labels)
angles = np.arange(0, 2*np.pi, sector_angle)
ax.bar(angles, data, color=plt.cm.Set3(np.arange(len(data_labels))/len(data_labels)), width=sector_angle, edgecolor="white", label=data_labels)

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(angles)
ax.set_xticklabels(data_labels,fontsize=15, wrap=True, rotation=45)
ax.set_yticklabels([])

ax.set_title('Number of Government Resources Allocated to Public Policy in 2021', fontsize=15)
ax.legend(bbox_to_anchor=(0.5, 0.95))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_117.png')

plt.clf()