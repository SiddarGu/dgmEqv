
import matplotlib.pyplot as plt
import numpy as np

data_labels=['Research','Design','Manufacturing','Testing']
line_labels=['Area','ratio']
data=[[47,23,17,13]]

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot()
wedges, texts, autotexts = ax.pie(data[0], startangle=90, counterclock=False, 
                                 autopct='%1.1f%%', colors=['coral','dodgerblue','mediumspringgreen','mediumpurple'])
centre_circle = plt.Circle((0,0),0.7,color='white')
ax.add_artist(centre_circle)
ax.set_title('Science and Engineering Breakdown - 2023', fontsize=18)
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.2), fontsize=14, ncol=4)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_145.png', bbox_inches='tight')
plt.clf()