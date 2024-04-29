
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge

data_labels = ["Judicial Decisions", "Administrative Regulations", "Legislation", "Case Law"]
data = np.array([33, 27, 30, 10])
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

outer_colors = ["#0099CC", "#FF9900", "#66AA00", "#FF3300"]
wedges, texts, autotexts = ax.pie(data,
                                  labels=data_labels,
                                  colors=outer_colors,
                                  startangle=90,
                                  counterclock=False,
                                  autopct="%1.1f%%")

circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)

ax.legend(data_labels, loc="upper right", bbox_to_anchor=(1.2, 0.8))
ax.set_title("Legal System Overview - 2023")

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_81.png', dpi=200, bbox_inches='tight')
plt.clf()