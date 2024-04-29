
import matplotlib.pyplot as plt
import matplotlib.patches as patches

data_labels=['Education','Social Welfare','Infrastructure','Security','Transparency']
data=[30,22,25,15,8]
line_labels=['Sector']

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)
ax.set_title('Government and Public Policy Overview - 2023')

ax.pie(data, labels=data_labels, colors=['#F09819','#FFB800','#F26C4F','#7F8C8D','#ABB7B7'], startangle=90, counterclock=False, wedgeprops={'linewidth':2})
circle = patches.Circle((0,0), 0.75, color='white')
ax.add_artist(circle)
ax.legend(data_labels,loc='upper center', bbox_to_anchor=(0.5, -0.1))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_66.png')
plt.clf()