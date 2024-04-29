
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show

data_labels = ['Court Rulings','Regulatory Compliance','Legal Advice','Representation','Litigation']
data = [30,20,20,15,15]
line_labels = ['Issue','Ratio']
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, colors=['red','green','blue','orange','cyan'], startangle=90, counterclock=False)
inner_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(inner_circle)
ax.set_title('Legal Affairs Outlook - 2023')
ax.legend(data_labels, loc="best", bbox_to_anchor=(1,1), bbox_transform=ax.transAxes)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_61.png')
plt.clf()