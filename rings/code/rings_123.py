
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

data_labels = ["Fundraising", "Donations", "Grants", "Volunteer Work", "Awareness"]
data = [12, 35, 25, 8, 20]
line_labels = ["Category", "ratio"]

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('equal')
ax.pie(data, labels=data_labels, textprops={'fontsize':14}, startangle=90, counterclock=False, colors=cm.viridis(np.linspace(0,1,len(data))))
center_circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(center_circle)
ax.legend(data_labels, loc="lower left", bbox_to_anchor=(0.5, -0.2), fontsize=14)
ax.set_title('Nonprofit Organizational Performance - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_75.png')
plt.clf()