
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Ticket Sales', 'Merchandise', 'Sponsorship', 'Media Rights', 'Advertising']
data = [20, 15, 25, 25, 15]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

ax.pie(data, startangle=90, counterclock=False, labels=data_labels, colors=[
       'red', 'green', 'blue', 'yellow', 'orange'])
centre_circle = plt.Circle((0, 0), 0.6, color='black', fc='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.legend(data_labels, loc="lower right")
ax.set_title('Sports and Entertainment Industry Overview - 2023')

plt.grid(True)
plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_135.png')
plt.clf()