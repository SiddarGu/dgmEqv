
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

data_labels=['Tourism Industry','Hospitality Services','Customer Service','Tourist Attractions','Revenue Generation']
data=[0.25,0.32,0.18,0.12,0.13]
line_labels=['Category','ratio']

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot()
ax.pie(data,startangle=90,counterclock=False,colors=['red','blue','orange','green','purple'])
circle=Circle(xy=(0,0),radius=0.5,fc='white')
ax.add_artist(circle)
ax.legend(data_labels,loc='upper right')
plt.title("Tourism and Hospitality Industry Performance - 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_42.png')
plt.clf()