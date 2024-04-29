
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Employee Retention", "Training & Development", "Performance Management", "Employee Engagement", "Payroll Management"]
data = [20, 15, 30, 20, 15]
line_labels = ["Category", "Ratio"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

wedges, texts, autotexts = ax.pie(data, startangle=90, counterclock=False, autopct='%.1f%%')
for i in range(len(wedges)):
    wedges[i].set_color(plt.cm.tab10(i))

circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)

ax.legend(data_labels, loc='upper right')
ax.set_title("Human Resources Management Overview - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_68.png")
plt.clf()