
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

data_labels = ['Mental Health','Physical Health','Nutrition','Exercise']
data = [44,31,9,16]
line_labels = ['Category']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['red', 'green', 'blue', 'yellow'])

centre_circle = Circle((0,0), 0.70, color='white')
ax.add_artist(centre_circle)

ax.set_title('Overall Health Status - 2023')
ax.legend(data_labels, loc='best')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_29.png')
plt.clf()