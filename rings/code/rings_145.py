
import matplotlib.pyplot as plt
import numpy as np

data_labels=['Disease Prevention', 'Vaccination Rate', 'Treatment Outcome', 'Hospital Quality', 'Patient Satisfaction']
data = [0.36, 0.15, 0.17, 0.16, 0.16]
line_labels = ['Category']

fig, ax = plt.subplots(figsize=(8,8))
ax.pie(data, startangle=90, counterclock=False)
circle = plt.Circle((0,0),0.5, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc="best")
ax.set_title('Healthcare Quality Indicators - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_106.png')
plt.cla()