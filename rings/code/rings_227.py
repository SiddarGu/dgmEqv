
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Get data
data_labels = np.array(['Spectator Attendance', 'Media Coverage', 'Sponsorship', 'Player Performance', 'Merchandise Sales'])
line_labels = np.array(['Category', 'ratio'])
data = np.array([29, 12, 22, 20, 17]).reshape(-1,1)

# Create chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.pie(data[:,0], labels = data_labels, startangle = 90, counterclock = False)
white_circle = plt.Circle((0, 0), 0.7, color = 'white')
ax.add_artist(white_circle)
ax.legend(data_labels, loc="center")
plt.title('Sports and Entertainment Performance Overview - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_9.png')
plt.gcf().clear()