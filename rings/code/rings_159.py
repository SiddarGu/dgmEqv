
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Sports Events", "Music Concerts", "Movie Premieres", "Gaming Competitions", "Online Streams"]
data = [0.28, 0.17, 0.15, 0.12, 0.28]
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['b', 'g', 'r', 'c', 'm'])

circle = plt.Circle((0, 0), 0.5, color="white")
ax.add_artist(circle)

ax.legend(data_labels, loc="best")
ax.set_title("Entertainment and Sports Industry - 2023")

plt.tight_layout()
fig.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_128.png")
plt.clf()