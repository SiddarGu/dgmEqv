

import matplotlib.pyplot as plt
import matplotlib.patches as patches

data_labels = ['Research and Development', 'Engineering', 'Data Analysis', 'Technical Support', 'Project Management']
data = [37, 20, 19, 15, 9]
line_labels = ['Area', 'ratio']

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock=False, colors=['red', 'green', 'purple', 'orange', 'blue'])
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)

ax.set_title('Science and Engineering Performance - 2023')
ax.legend(data_labels, loc='best', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_44.png')
plt.clf()