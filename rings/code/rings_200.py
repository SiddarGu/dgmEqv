
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

data_labels = ["Research", "Robotics", "Automation", "Software", "Electronics"]
data = [25, 17, 15, 18, 25]
line_labels = ["Domain"]

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
wedges, texts, autotexts = ax.pie(data, colors=['#FF8C00', '#87CEFA', '#1E90FF', '#00CD00', '#CD5C5C'], autopct='%1.1f%%', startangle=90, counterclock=False)
centre_circle = plt.Circle((0,0),0.5,color='white')
ax.add_artist(centre_circle)
ax.legend(data_labels, loc="best")
ax.set_title("Science and Engineering Advancement - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_53.png")
plt.clf()