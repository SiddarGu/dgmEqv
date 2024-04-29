
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Renewable Sources", "Fossil Fuels", "Nuclear Power", "Conservation", "Efficiency"]
data = [42, 36, 8, 10, 4]
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['orange', 'red', 'purple', 'green', 'blue'])
centre_circle = plt.Circle((0,0),0.60,fc='white')
ax.add_artist(centre_circle)
ax.legend(data_labels, loc="best")
plt.title("Energy Consumption Patterns - 2023", fontsize=14)
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_113.png")
plt.clf()