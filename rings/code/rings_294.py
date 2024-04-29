
import matplotlib.pyplot as plt
import numpy as np

data_labels=["Academic Excellence","Facilities","Student/Teacher Ratio","Classroom Engagement","Career Readiness"]
data=[0.25,0.15,0.1,0.25,0.25]
line_labels=["Category","Ratio"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, colors=['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF'], startangle=90, counterclock=False)
c = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(c)
ax.set_title('Education Quality Evaluation - 2023', fontsize=20)
ax.legend(data_labels, loc="upper right", fontsize=14, bbox_to_anchor=(1.2, 0.8))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_25.png')
plt.clf()