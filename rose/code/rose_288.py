
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Music','Movies','Sports','Gaming','Animation','Theater']
line_labels = ['Category','Number']
data = np.array([[50,30,20,15,10,5]])

#plot the data with the type of rose chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, polar=True)
sector_angle = (2 * np.pi) / len(data_labels)

#assign a different color to each sector
colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']

#draw sectors corresponding to different categories
for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, color=colors[i], label=data_labels[i])

#set the number of ticks
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))

#set the category labels
ax.set_xticklabels(data_labels, fontdict={'fontsize': 14}, rotation=45)

#add legend
ax.legend(bbox_to_anchor=(1, 0.5), loc="center left")

#set title
plt.title('Popularity of Entertainment and Sports in 2021', fontdict={'fontsize': 20})

#automatically resize the image
plt.tight_layout()

#Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_92.png')

#clear the current image state
plt.clf()