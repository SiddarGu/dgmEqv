
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ["Academic Performance", "Student Engagement", "Graduate Retention", 
               "Quality of Faculty", "Campus Satisfaction"]
data = np.array([30, 25, 15, 20, 10])
line_labels = ["Category", "ratio"]

fig, ax = plt.subplots(figsize=(10, 7))

ax.pie(data, startangle=90, counterclock=False, wedgeprops=dict(width=0.3))
ax.add_artist(plt.Circle((0, 0), 0.7, color='white'))
ax.legend(data_labels, loc="best")

plt.title("Educational Progress - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_6.png")
plt.clf()