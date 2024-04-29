
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

data_labels = ['Court Cases', 'Lawsuits', 'Legislation', 'Contracts', 'Appeals']
data = np.array([45, 15, 12, 21, 7])
line_labels = ['Variable','Ratio']

fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(111)
patches, texts, autotexts = ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%1.1f%%')
ax.set_title("Legal System Trends - 2023")

# Adjust the radius of the inner circle to create different ring widths.
centre_circle = plt.Circle((0,0),0.8,fc='white')

for text in texts:
    text.set_rotation(0)
    text.set_wrap(True)

# Add the white circle to the center of the pie chart.
ax.add_artist(centre_circle)
ax.legend(data_labels, labelspacing=1, loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_133.png')
plt.clf()