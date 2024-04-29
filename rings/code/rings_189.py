
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Art Projects","Cultural Events","Education","Heritage Preservation","Media"]
data = [18,42,25,7,8]
line_labels = ["Category","ratio"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#f73468', '#f8a903', '#3cb9d8', '#f7921e', '#4aaee9'])
circle = plt.Circle(xy=(0,0), radius=0.75, fc='white')
ax.add_artist(circle)
ax.legend(data_labels, loc="upper right")
plt.title("Arts and Culture Investment - 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_36.png')
plt.clf()