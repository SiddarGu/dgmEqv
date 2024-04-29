
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Education', 'Culture', 'Social Interactions', 'Human Development', 'Values']
data = [31, 13, 30, 18, 8]
line_labels=['Category', 'ratio']

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
ax.axis('equal') # Set aspect ratio to be equal so it is a circle

ax.pie(data, labels=data_labels, startangle=90, counterclock=False,
       wedgeprops=dict(width=0.3, edgecolor='white'))

# Draw a circle to make the pie chart look like a ring
centre_circle = plt.Circle((0,0),0.7,fc='white')
ax.add_artist(centre_circle)

ax.set_title('Humanities and Social Sciences - 2023')
ax.legend(data_labels, bbox_to_anchor=(1.2, 1.1))
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_12.png')
plt.clf()