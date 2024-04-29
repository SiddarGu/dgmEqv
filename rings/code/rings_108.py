
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

data_labels = ['Education', 'Arts', 'Social Sciences', 'Humanities']
data = [27, 19, 10, 44]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot()
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#5f9ea0', '#d2691e', '#ff8c00', '#6495ed'])
circle = Circle((0, 0), 0.7, facecolor='white')
ax.add_artist(circle)
ax.legend(data_labels)
ax.set_title('Academic Performance in Social Sciences and Humanities - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_59.png')
plt.clf()