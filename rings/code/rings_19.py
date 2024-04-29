
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

data_labels = ['Education','Arts','Humanities','Social Sciences']
data = [0.4, 0.2, 0.15, 0.25]
line_labels = ['Domain']

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111)

wedges, texts = ax.pie(data, colors=['#FFC62F','#F25F5C','#247BA0','#70C1B3'], startangle=90, counterclock=False, labels=data_labels, wedgeprops={'linewidth': 1})
circle = Circle((0, 0), 0.6, color='white', fc='white', linewidth=0)
ax.add_artist(circle)
ax.legend(data_labels, loc='upper right')
ax.set_title('Social Sciences and Humanities Overview - 2023', fontsize=14)

for i in range(len(wedges)):
    wedges[i].set_linewidth(1)
    wedges[i].set_edgecolor('black')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_3.png')
plt.clf()