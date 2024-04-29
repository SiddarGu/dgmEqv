
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Vaccination", "Chronic Diseases", "Mental Health", "Accessibility", "Prevention"]
data = np.array([47, 19, 13, 13, 8])
line_labels = ["Category", "ratio"]

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%', colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc="upper right")
ax.set_title("Health Priorities - 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_1.png')
plt.clf()