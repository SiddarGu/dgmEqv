
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ['Delivery Efficiency', 'Fuel Efficiency', 'Vehicle Maintenance', 'Safety', 'Staff Performance']
data = [33,7,15,20,25]
line_labels = ['Category', 'Ratio']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
wedges, texts = ax.pie(data, startangle=90, counterclock=False, colors=['dodgerblue', 'royalblue', 'navy', 'teal', 'mediumseagreen'], 
                        wedgeprops={'linewidth': 2, 'edgecolor': 'white'}, 
                        textprops={'fontsize': 12, 'color': 'white'})
centre_circle = plt.Circle((0,0),0.7,color='white', fc='white',linewidth=2)
ax.add_artist(centre_circle)
ax.set_title('Logistics Performance Assessment - 2023', fontsize=16, fontweight='bold')
ax.legend(data_labels, fancybox=True, shadow=True, bbox_to_anchor=(0.9,0.9), fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_12.png')
plt.clf()