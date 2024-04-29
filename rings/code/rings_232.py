
import matplotlib.pyplot as plt

data_labels = ['Cultural Awareness','Arts Appreciation','Creative Thinking','Aesthetic Sensitivity','Artistic Expression']
data = [25,20,35,17,3]
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, colors=plt.cm.rainbow(np.linspace(0, 1, len(data))), startangle=90, counterclock=False, autopct='%.2f%%')
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.set_title('Arts and Culture Competence - 2023')
ax.legend(data_labels, loc="best")
ax.grid(True)
plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_98.png')
plt.clf()