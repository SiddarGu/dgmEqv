
import matplotlib.pyplot as plt 
import numpy as np 

data_labels=["Cultural Awareness", "Art Education", "Creative Expression", "Cultural Preservation", "Public Engagement"] 
data=[0.35, 0.1, 0.25, 0.2, 0.1] 
line_labels=["Category", "ratio"] 

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111) 
ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%', colors=['#f3622d', '#fba71b', '#57b757', '#41a9c9', '#4258c9']) 
ax.set_title('Arts and Culture Impact - 2023') 
circle = plt.Circle((0,0), 0.7, color='white') 
ax.add_artist(circle)
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1, 0.8), fontsize=12)
ax.axis('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_23.png')
plt.clf()