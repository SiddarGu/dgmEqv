
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Taxation', 'Regulatory Compliance', 'Financial Reporting', 'Cost Control', 'Risk Management']
data = np.array([21, 12, 18, 22, 27])
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False)
centre_circle = plt.Circle((0, 0), 0.60, color='white')
ax.add_artist(centre_circle)
ax.legend(data_labels, loc='upper left')
plt.title("Financial Management Overview - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_68.png")
plt.clf()