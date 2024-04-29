

import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Ticket Sales", "Media Rights", "Merchandise", "Sponsorships"]
data = np.array([33, 23, 19, 25])
line_labels = ["Category","ratio"]

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['#ff7f0e', '#d62728', '#2ca02c', '#1f77b4']) 
inner_circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(inner_circle)
ax.legend(data_labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Sports and Entertainment Profitability - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_130.png")
plt.clf()