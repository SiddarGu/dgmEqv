
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Public Transport", "Road Freight","Air Freight", "Rail Freight"]
data = [30, 45, 20, 5]
line_labels = ["Mode", "ratio"]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors = ['#4f9cde', '#ff8c00', '#2f52a0','#dc2d2b'])
circle = plt.Circle((0,0), 0.75, color='white', lw=1, edgecolor='white')
ax.add_artist(circle)
ax.set_title("Transportation and Logistics Analysis - 2023", fontsize=14)
ax.legend(data_labels, loc="upper right", bbox_to_anchor=(1.1, 0.8))
plt.grid(True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_85.png")
plt.clf()