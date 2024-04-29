
import matplotlib.pyplot as plt
import numpy as np

#transform data
data_labels = ['Social Media','Web Development','Digital Marketing','Online Advertising','Search Engine Optimization','Web Design','E-Commerce','Network Security','Cyber Security']
data = [90,80,70,60,50,40,30,20,10]
line_labels = ['Category','Number']

#create figure
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='polar')

#plot data
colors = ['#ff9999','#ffcc99','#66b3ff','#99ff99','#ffb3e6','#c2c2f0','#ffb3e6','#ff6666','#ffff99']
sector_angle = (2 * np.pi) / len(data_labels)

for i, label in enumerate(data_labels):
    ax.bar(i*sector_angle, data[i], width=sector_angle, color=colors[i], label=label)

#set tick label
ax.set_xticks(np.arange(0, 2*np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=20)

#legend
ax.legend(data_labels, bbox_to_anchor=(1.1, 1.1))

#title
plt.title("Usage of Online Technologies in 2021", fontsize=20)

#tight layout
plt.tight_layout()

#save
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_109.png')

#clear
plt.clf()