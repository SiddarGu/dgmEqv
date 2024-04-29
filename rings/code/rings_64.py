
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

data_labels=["Vaccination Coverage","Health Education","Disease Control","Mental Health Support","Health Insurance"]
data=[30,20,20,15,15]
line_labels=['Category']

fig, ax = plt.subplots(figsize=(10,5))
ax.pie(data, startangle=90,counterclock=False)
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.7))
ax.set_title('Health and Well-being Indicators - 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_132.png')
plt.close()