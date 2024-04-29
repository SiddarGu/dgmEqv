
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Education Quality','Social Welfare','Cultural Development','Infrastructure','Human Rights'] 
data = [36,11,20,10,23] 
line_labels = ['Category','ratio'] 

fig = plt.figure(figsize=(8, 8)) 
ax = fig.add_subplot(111) 
ax.pie(data, labels=data_labels, startangle=90, counterclock=False) 
circle = plt.Circle((0,0),0.7,color='white')
ax.add_artist(circle) 
ax.set_title('Social Sciences and Humanities Overview - 2023')
ax.legend(data_labels) 
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_38.png') 
plt.clf()