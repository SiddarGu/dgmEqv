
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[18,68,47,42,73,29,53,23]])
data_labels = ["Web Design","Social Media Management","Search Engine Optimization","Cyber Security","Digital Marketing","Web Content Writing","Web Development","Mobile App Development"]
line_labels = ["Number"]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")

sector_angle = (2 * np.pi) / len(data_labels)
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[0][i], width=sector_angle, bottom=0.0, color=plt.cm.Set1(i/len(data_labels)), label=data_labels[i])

ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, rotation=90, wrap=True, fontsize=10)
ax.legend(bbox_to_anchor=(1.3,1), loc="upper right")

ax.set_title("Number of Professionals Employed in the Social Media and Web Industries", y=1.08)

plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_10.png")
plt.clf()