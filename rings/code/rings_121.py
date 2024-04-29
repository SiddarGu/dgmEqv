
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Product Quality", "Production Speed", "Resource Utilization", "Delivery Performance", "Cost Management"]
data = [20, 30, 15, 20, 15]
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['red','orange','green','blue','purple'])
circle = plt.Circle(xy=(0, 0), radius=0.5, edgecolor='white', facecolor='white')
ax.add_artist(circle)
ax.legend(data_labels, loc='upper left')
plt.title("Manufacturing & Production Performance - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_72.png")
plt.clf()