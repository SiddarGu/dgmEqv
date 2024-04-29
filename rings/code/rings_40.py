
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

data_labels = ['Sports', 'Music', 'Movies', 'Gaming', 'Art']
data = [0.35, 0.15, 0.2, 0.25, 0.05]
line_labels = ['Type', 'Ratio']

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
center_circle = Circle((0,0), 0.7, color='white')
ax.add_artist(center_circle)
ax.set_title('Popular Entertainment Trends - 2023')
ax.legend(data_labels, loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_5.png')
plt.clf()