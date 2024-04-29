
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Customer Acquisition", "Online Sales", "Advertising", "Inventory Management", "Customer Retention"]
data = [17, 33, 25, 10, 15]
line_labels = ["Category", "Ratio"]

fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%1.1f%%')

circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)

ax.legend(data_labels, loc='center left', bbox_to_anchor=(0.9, 0.5))
ax.set_title("Retail and E-commerce Performance - 2023")
plt.tight_layout()
fig.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_32.png")
plt.clf()