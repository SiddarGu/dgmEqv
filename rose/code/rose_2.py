
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Education","Health","Poverty","Homelessness","Environment","Human Rights","Community Development","Animal Welfare"]
data = np.array([40,90,50,30,70,60,20,10])
line_labels = ["Category","Number"]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i])
ax.set_thetagrids(np.arange(0, 360, 360/num_categories), labels=data_labels)
ax.set_title('Number of Nonprofits Engaged in Different Fields in 2021', fontsize=15, y=1.1)
ax.legend(bbox_to_anchor=(1.2, 0.75))

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/2.png')
plt.tight_layout()
plt.clf()