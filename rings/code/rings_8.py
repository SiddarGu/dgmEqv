
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Employee Retention", "Training and Development", "Performance Evaluation", "Hiring and Recruitment", "Benefits Management"]
data = [41, 12, 11, 19, 17]
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, startangle=90, counterclock=False)
center_circle = plt.Circle((0,0), 0.70, color='white')
ax.add_artist(center_circle)
ax.axis('equal')
ax.set_title("Human Resources and Employee Management - 2023")
ax.legend(data_labels, loc="upper left", bbox_to_anchor=(-0.1, 1.))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_14.png')
plt.clf()