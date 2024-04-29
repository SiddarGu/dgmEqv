
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Connectivity','Security','Data Traffic','Innovation','User Experience']
line_labels = ['Category','ratio']
data = np.array([[26,7,25,13,29]])

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, aspect='equal')

colors = plt.cm.tab10(np.arange(5))

ax.pie(data[0], labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False, colors=colors)

centre_circle = plt.Circle((0,0),0.7,fc='white')
ax.add_artist(centre_circle)

ax.legend(data_labels,loc='upper left')

plt.title('Technology and the Internet Trends - 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_6.png')

plt.clf()