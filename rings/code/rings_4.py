
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Average Price','Home Sales','Mortgage Rates','Investment Yields','Vacancy Rates']
data = [29,17,14,18,22]
line_labels = ['Category','ratio']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(5)*4)

ax.pie(data, colors=outer_colors,
       labels=data_labels,
       startangle=120,
       counterclock=False,
       wedgeprops=dict(width=0.5, edgecolor='w'))

inner_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(inner_circle)

ax.set_title('Real Estate and Housing Market Overview - 2023', fontsize=20)
ax.legend(data_labels, loc="upper left", bbox_to_anchor=(1.1, 0.7))
ax.axis('equal')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122217_5.png')
plt.cla()