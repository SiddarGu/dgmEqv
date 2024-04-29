
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches 

data_labels = ['Artistic Expression','Cultural Heritage','Arts Education','Artist Support','Quality Artworks']
data = [0.28, 0.19, 0.17, 0.20, 0.16]
line_labels = ['Category', 'ratio']

fig, ax = plt.subplots(figsize=(7,7))

ax.pie(data, startangle=90, counterclock=False, wedgeprops=dict(width=0.4))
inner_circle = mpatches.Circle(xy=(0,0), radius=0.6, facecolor='white')
ax.add_artist(inner_circle)
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(1.0,0.5))

ax.set_title('Arts and Culture Development - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122217_3.png')
plt.clf()