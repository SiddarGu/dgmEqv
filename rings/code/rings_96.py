
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Donations", "Volunteers", "Fundraising", "Grants", "Community Engagement"]
data = [31, 17, 21, 15, 16]
line_labels = ["Category", "Ratio"]

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(data, startangle=90, counterclock=False, labels=data_labels)
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.axis('equal')
ax.legend(data_labels, fontsize=15)

plt.title('Nonprofit Organization Impact - 2023', fontsize=15)
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_39.png")
plt.clf()