
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Education", "Taxation", "International Relations", "Budget", "Social Welfare", "Infrastructure", "Trade", "Environmental", "National Security"]
data = [150, 200, 80, 90, 125, 110, 45, 70, 30]
line_labels = ["Education", "Taxation", "International Relations", "Budget", "Social Welfare", "Infrastructure", "Trade", "Environmental", "National Security"]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i],width=sector_angle,label=line_labels[i])

ax.legend(data_labels,bbox_to_anchor=(1.1,1.05))
ax.set_xticks(np.linspace(sector_angle/2,2*np.pi,num_categories,endpoint=False))
ax.set_xticklabels(data_labels, wrap=True)
plt.title("Number of Public Policies in 2021")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_17.png")
plt.clf()