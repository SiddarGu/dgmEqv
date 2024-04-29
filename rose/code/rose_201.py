
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Painting","Sculpture","Theatre","Photography","Calligraphy","Music","Dance","Poetry","Cinema"]
data = [90,80,50,43,40,36,30,20,10]
line_labels = ["Art Form","Number of Participants"]

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111, polar=True)
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i*sector_angle, data[i], width=sector_angle, color=plt.cm.Set1(i/num_categories), label=data_labels[i])

ax.legend(bbox_to_anchor=(1.2, 1.05), loc='upper left')

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=45, fontsize=15, wrap=True)

ax.set_title(label="Popularity of Art Forms Amongst Participants in 2021", fontweight='bold', fontsize=20, pad=20)

plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_50.png")
plt.clf()