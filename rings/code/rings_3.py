
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Quality Control', 'Production Times', 'Maintenance', 'Cost Efficiency', 'Resources Usage']
line_labels = ['Metric', 'ratio']
data = np.array([[17, 12, 5, 50, 16]])

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(data.flatten(), labels=data_labels, startangle=90, counterclock=False)
circle = plt.Circle((0, 0), 0.6, color='white')
ax.add_artist(circle)

ax.legend(data_labels, loc='upper left')
ax.set_title('Manufacturing and Production Overview - 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122217_4.png')
plt.clf()