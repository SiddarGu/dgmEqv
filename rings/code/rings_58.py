
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Materials Usage","Efficiency","Quality Control","Automation","Production Capacity"]
data = [25,20,10,30,15]
line_labels = ["Category","ratio"]

fig,ax = plt.subplots(figsize=(8,6))
ax.pie(data, labels=data_labels, startangle=90, counterclock=False)
inner_circle = plt.Circle((0,0), 0.5, color="white")
ax.add_artist(inner_circle)
ax.legend(data_labels, loc="upper right")
ax.set_title("Manufacturing and Production Overview - 2023")
ax.axis('equal')

plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_123.png")
plt.clf()