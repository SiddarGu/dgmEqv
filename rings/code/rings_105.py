
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Mechanical Engineering","Computer Science","Civil Engineering","Materials Science","Physics"]
data = [20,30,15,7,28]
line_labels = ["Field","ratio"]

fig, ax = plt.subplots(figsize=(12, 6)) 
ax.pie(data, startangle=90,counterclock=False)
centre_circle = plt.Circle((0,0),0.7,fc='white')
ax.add_artist(centre_circle)
ax.set_title("Breakdown of Science and Engineering Disciplines - 2023")
ax.legend(data_labels, bbox_to_anchor=(1, 0.8))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_55.png')
plt.clf()