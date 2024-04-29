
import matplotlib.pyplot as plt
import numpy as np

data_labels = np.array(['Education', 'Infrastructure', 'Social Welfare', 'Economy', 'Security'])
data = [23, 17, 15, 35, 10]
line_labels = np.array(['Education', 'Infrastructure', 'Social Welfare', 'Economy', 'Security'])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
ax.pie(data, labels=line_labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, counterclock=False, explode=explode)

# create a white circle for the center of the pie chart
centre_circle = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(centre_circle)

# create a legend
ax.legend(data_labels, loc='upper right')
ax.set_title('Government and Public Policy Impact - 2023')
fig.tight_layout()

fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_37.png')
plt.clf()