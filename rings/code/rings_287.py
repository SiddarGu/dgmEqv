
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches 
import numpy as np 

data_labels = ['Resource Consumption','Energy Usage','Pollution Reduction','Waste Management','Biodiversity'] 
data = [25,15,20,25,15] 
line_labels = ['Category','ratio'] 

fig, ax = plt.subplots(figsize=(14,7)) 
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#e6194b','#3cb44b','#ffe119','#4363d8','#f58231']) 
circle = mpatches.Circle((0,0), 0.75, color='white') 
ax.add_artist(circle) 
ax.set_title('Sustainability Performance Report - 2023') 
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5) 
ax.axis('equal') 
plt.tight_layout() 

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_15.png') 
plt.clf()