
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Renewable Energy", "Fossil Fuels", "Nuclear Energy", "Hydroelectricity", "Natural Gas"]
data = [33, 27, 15, 10, 15]
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.pie(data, labels = data_labels, startangle = 90, counterclock = False, 
      colors = ['#00ccff', '#9900cc', '#0099cc', '#33cc33', '#cccc00'])
center_circle = plt.Circle((0,0), 0.7, color = 'white')
ax.add_artist(center_circle)
ax.legend(data_labels, loc = 'upper right')
ax.set_title('Energy Utilization in 2023', fontsize = 20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_80.png')
plt.cla()