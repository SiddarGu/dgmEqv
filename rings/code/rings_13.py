
import matplotlib.pyplot as plt
import numpy as np

# transform data
data_labels = ['Network Security', 'Data Storage', 'Cloud Computing', 'Automation', 'Network Reliability']
data = [30, 15, 25, 20, 10]
line_labels = ['Category', 'Ratio']

# plot figure
fig = plt.figure(figsize=(10,5))  # set figsize
ax = fig.add_subplot()  # add subplot
ax.set_title('Technology and the Internet - 2023')  # set title
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=plt.cm.Set1.colors)  # plot piechart

# change pie chart to ring chart
inner_circle = plt.Circle((0,0), 0.6, color='white')  # create a white circle
ax.add_artist(inner_circle)  # add the white circle to ax

ax.legend(data_labels, loc='best')  # plot legend

plt.grid(True)  # add grid background
plt.tight_layout()  # resize the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_22.png')  # save the figure
plt.clf()  # clear the current image state