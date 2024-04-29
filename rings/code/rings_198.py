

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

data_labels = ["Spectator Participation", "Athlete Performance", "Viewership", "Merchandising", "Media Coverage"]
data = [17, 35, 20, 13, 15]
line_labels = ["Category", "Ratio"]

fig, ax = plt.subplots(figsize=(7,7))
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%1.1f%%')
# Create white circle to make the chart looks like a ring
centre_circle = Circle((0,0), 0.60, fc='white')
ax.add_artist(centre_circle)
ax.legend(data_labels, loc='lower left')
plt.title('Sports and Entertainment Industry Overview - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_48.png')
plt.clf()