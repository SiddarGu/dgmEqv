
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ['Humanities','Social Sciences','Arts and Culture','Communications','Language','Recreation','History','Physical Education','Literature']
data = [240,350,150,100,90,60,80,40,20]
line_labels = ['Course Type','Number of Students']

fig = plt.figure(figsize=(10, 8)) 
ax = fig.add_subplot(111, polar=True) 
num_categories = len(data_labels) 
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories): 
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i]) 

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle)) 
ax.set_xticklabels(data_labels, fontsize=10, rotation=90) 
ax.legend(bbox_to_anchor=(1.05, 1.0)) 

ax.set_title('University Enrollment by Course Type in 2021', fontsize=14) 
plt.tight_layout() 
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_16.png') 
plt.clf()