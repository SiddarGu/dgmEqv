
import matplotlib.pyplot as plt
import numpy as np

data_labels = np.array(["Viewership", "Attendance", "Sponsorship", "Advertising", "Merchandise"])
data = np.array([51, 20, 14, 10, 5])
line_labels = np.array(["Category", "ratio"])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.pie(data, labels=data_labels, startangle=90, counterclock=False,autopct='%1.1f%%', colors=['red','blue','green','violet','orange'])
circle = plt.Circle((0,0), 0.70, color='white')
ax.add_artist(circle)

ax.set_title("Sports and Entertainment Revenue - 2023")
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1, 0.7), fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_150.png')
plt.clf()