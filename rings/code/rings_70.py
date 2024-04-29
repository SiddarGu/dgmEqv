
import matplotlib.pyplot as plt
import numpy as np

data_labels = np.array(["Digital Connectivity", "Innovation", "Automation", "User Experience", "Security"])
data = np.array([18, 27, 17, 20, 18])
line_labels = np.array(["Category", "ratio"])

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
ax.pie(data, startangle=90, counterclock = False, colors=['#FFA500','#00FF00','#0000FF','#FFFF00','#FF00FF'])
centre_circle = plt.Circle((0,0),0.50,color='white')
ax.add_artist(centre_circle)
ax.set_title("Technology and the Internet - Analysis of Trends in 2023")
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.5), loc="center right", fontsize=12)
plt.axis('equal')
plt.grid(True,axis='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_139.png")
plt.clf()