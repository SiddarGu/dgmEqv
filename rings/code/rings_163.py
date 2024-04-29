
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Profits", "Expenses", "Investments", "Revenue", "Market Share"]
data = np.array([45, 25, 15, 10, 5])
line_labels = ["Category", "Ratio"]

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(data, labels=data_labels, startangle=90, counterclock=False)

centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax.axis('equal')
ax.legend(data_labels, loc="upper left")
ax.set_title("Financial Analysis - 2025")

plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_135.png")
plt.clf()