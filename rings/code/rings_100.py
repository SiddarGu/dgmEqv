
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Efficiency","Quality","Cost Control","Resource Utilization","Safety Performance"]
line_labels = ["Aspect","ratio"]

data = np.array([[20,39,6,15,20]])

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
wedges, texts, autotexts = ax.pie(data[0], startangle=90, counterclock=False, colors=['#007AFF', '#FFCA00', '#FF2E00', '#ADADAD', '#0BBD2F'], autopct='%1.1f%%')
inner_circle = plt.Circle((0,0), radius=0.5, color='white')
ax.add_artist(inner_circle)

ax.legend(data_labels, loc="upper left")
ax.set_title("Manufacturing and Production Performance - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_48.png")
plt.clf()