
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Full-time Employees","Part-time Employees","Contractors","Interns","Trainees"]
data = [420,110,120,60,30]
line_labels = ["Employee Type","Number"]

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Dark2(i))

ax.set_theta_direction(-1)
plt.xticks(np.arange(0, num_categories) * sector_angle, data_labels, color='black', size=12)

ax.set_title("Employee Count by Type in a Company", fontsize=14)
ax.legend(bbox_to_anchor=(1.1, 1.1))
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_44.png')

plt.clf()