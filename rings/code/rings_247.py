
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

data_labels = ["Sporting Events", "Music Concerts", "Movies and TV", "Gaming", "Other Entertainment"]
data = np.array([24, 20, 31, 15, 10])
line_labels = ["Category", "ratio"]

fig, ax = plt.subplots(figsize=(8,8))

ax.pie(data, startangle=90, counterclock=False, wedgeprops={'width': 0.3}, colors=['#000099', '#006600', '#FFFF00', '#FF0000', '#663300'])
circle = plt.Circle((0,0), 0.5, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc=2, fontsize=15)
ax.set_title("Entertainment and Sports Scene in 2023", fontsize=18, pad=20)
ax.axis('equal')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_5.png')
plt.clf()