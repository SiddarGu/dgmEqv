
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Media Coverage","Stadium Attendance","Merchandise Sales","Ticket Sales","Sponsorship"]
data = np.array([23, 18, 15, 19, 25])
line_labels = ["Category","ratio"]

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(1, 1, 1)
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, counterclock = False)
centre_circle = plt.Circle((0,0),0.75,color='white', fc='white',linewidth=1.25)
ax.add_artist(centre_circle)
ax.legend(data_labels, loc="upper right")
plt.title("Sports and Entertainment Industry Performance - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_123.png")
plt.clf()