
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines

data_labels = ['Raw Material Cost', 'Production Cost', 'Shipping and Delivery', 'Marketing']
line_labels = ['Category']
data = [[30, 42, 8, 20]]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data[0], labels=data_labels, startangle=90, counterclock=False, autopct='%.2f%%')

plt.title('Food and Beverage Industry Cost Breakdown - 2023', fontsize=20, wrap=True)
circle = patches.Circle((0, 0), radius=0.7, facecolor='white', edgecolor='black')
ax.add_artist(circle)
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(1, 0.8))
ax.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_29.png')
plt.clf()