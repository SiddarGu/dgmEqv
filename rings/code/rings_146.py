
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Renewable Energy', 'Storage Capacity', 'Power Generation', 'Energy Transmission', 'Energy Efficiency']
data = [19, 27, 30, 17, 7] 
line_labels = ['Category','ratio']

fig, ax = plt.subplots(figsize=(12, 6))

ax.pie(data, startangle=90, counterclock=False, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#FFE4C4'])
circle = plt.Circle((0,0), 0.70, color='white')
ax.add_artist(circle)
ax.legend(data_labels,loc='lower center',bbox_to_anchor=(0.5, -0.2)) 
ax.set_title('Energy and Utilities Overview - 2023')
ax.grid(True)
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_108.png')
plt.clf()