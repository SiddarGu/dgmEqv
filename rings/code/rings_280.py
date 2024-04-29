
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

data_labels = ['Donations', 'Grants', 'Fundraising', 'Volunteer Hours', 'Charitable Events']
data = [17, 30, 12, 9, 32] 
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(7, 7)) 
ax = fig.add_subplot() 
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#d6f5f5', '#2e86c1', '#f7dc6f', '#f4d03f', '#e74c3c']) 
centre_circle = plt.Circle((0, 0), 0.60, fc='white') 
ax.add_artist(centre_circle) 
ax.set_title('Charitable Impact Analysis - 2023')
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1.25, 1.0), fontsize=12, 
          ncol=1, frameon=True, fancybox=True, shadow=True)
ax.grid(linestyle='--')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_140.png')
plt.clf()