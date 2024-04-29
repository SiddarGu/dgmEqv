
import matplotlib.pyplot as plt
import numpy as np

data_labels = np.array(["Ticket Sales", "Viewership", "Merchandise", "Advertising", "Sponsorship"])
data = np.array([20, 17, 14, 25, 24])
line_labels = ["Category", "Ratio"]

fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%1.1f%%')
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
plt.title("Sports and Entertainment Market Trends - 2023")
ax.legend(data_labels, loc='best', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122217_2.png')
plt.clf()