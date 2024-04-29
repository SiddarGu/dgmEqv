
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Climate Change","Renewable Energy","Sustainable Development","Water Conservation","Air Pollution","Waste Management","Biodiversity","Soil Pollution"]
data = [50,60,40,20,70,30,10,100]
line_labels = ["Topic","Number"]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar') 

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(len(data)):
    ax.bar([sector_angle * i], [data[i]], width = sector_angle, label=data_labels[i],color=np.random.rand(3,))

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

ax.legend(bbox_to_anchor=(1.2, 0.8))

plt.title("Global Sustainable Development Initiatives in 2021")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_139.png')
plt.close()