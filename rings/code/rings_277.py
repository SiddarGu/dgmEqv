
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_labels = ["Digital Adoption", "Mobile Usage", "Consumer Spending", "Online Security", "Innovation"]
data = [39, 25, 17, 14, 5]
line_labels = ["Category", "Ratio"]

fig = plt.figure(figsize = (15, 10))
ax = fig.add_subplot(111)
ax.pie(data, startangle = 90, counterclock = False,
       colors = ["#00FFFF", "#00FF00", "#FF00FF", "#FF0000", "#FFFF00"],
       autopct = '%1.1f%%')
circle = plt.Circle(xy = (0, 0), radius = 0.75, fc = 'white')
ax.add_artist(circle)
ax.legend(data_labels, bbox_to_anchor = (1.05, 1))
ax.set_title("Technology and Internet Trends - 2023", fontsize = 20)
plt.tight_layout()

plt.savefig(r'/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_137.png')
plt.clf()