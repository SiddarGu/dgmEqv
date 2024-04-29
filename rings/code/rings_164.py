
import matplotlib.pyplot as plt
import numpy as np
data_labels=['Equipment Maintenance','Cost Control','Quality Control','Logistics','Production Efficiency']
data=[24,20,18,13,25]
line_labels=['Category','ratio']

fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111)
ax.pie(data,labels=data_labels,autopct="%1.1f%%",startangle=90,counterclock=False,colors=['#006699','#cc6600','#cc9933','#009999','#cc0066'])
centre_circle=plt.Circle((0,0),0.75,color='white', fc='white',linewidth=2.25)
ax.add_artist(centre_circle)
ax.axis('equal')
ax.grid(True)
ax.legend(data_labels)
plt.title('Manufacturing and Production Performance Overview - 2023',fontsize=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_136.png')
plt.clf()