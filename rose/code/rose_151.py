
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Apparel","Electronics","Home Goods","Groceries","Toys","Tools","Automotive","Gardening","Pet Supplies","Sports"]
data = [100,120,80,200,90,60,70,50,40,30]
line_labels = ["Category","Number"]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

colors = ["red","orange","yellow","green","blue","indigo","violet","pink","brown","grey"]
sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, bottom=0.0, color=colors[i], label=data_labels[i])

ax.set_thetagrids(np.arange(0,360,360/len(data_labels)), labels=data_labels, fontsize=15)
ax.legend(bbox_to_anchor=(1.2,1.02), fontsize=15)

ax.set_title("Number of Retail and E-commerce Stores by Product Category in 2021", fontsize=18)
fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_37.png')
plt.clf()