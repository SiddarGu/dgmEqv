
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = [['Data Analytics', 21], ['Advertising', 10], ['Digital Presence', 39], ['Social Media', 15], ['Web Design', 15]]

data_labels = [item[0] for item in data]
data = [item[1] for item in data]
line_labels = ['']

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, wedgeprops = { 'linewidth' : 1 , 'edgecolor' : 'black'})

circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)

ax.set_title('Social Media and Web Performance - 2023')
ax.legend(data_labels, loc="upper left")

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_4.png')

plt.clf()