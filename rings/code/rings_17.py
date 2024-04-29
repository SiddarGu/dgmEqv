
import matplotlib.pyplot as plt
import numpy as np

data_labels=['Customer Ratings','Tourism Services','Hospitality Services','Travel Options','Tourist Attractions']
data=np.array([19,20,20,13,28])
line_labels=['Category','ratio']

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot()
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#36A2EB','#FF6384','#FFCE56','#c9daf8','#E7E9ED'])
centre_circle=plt.Circle((0,0),0.70,fc='white')
ax.add_artist(centre_circle)
ax.legend(data_labels, loc='upper left')
ax.set_title('Tourism and Hospitality - 2023')
plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_27.png')

plt.clf()