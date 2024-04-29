
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ["Tax Rates", "Budget Allocation", "Social Programs", "Foreign Relations", "Infrastructure"]
data = np.array([24, 14, 43, 12, 7])
line_labels = ["Category", "Ratio"]

fig, ax = plt.subplots(figsize=(10,10))
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, wedgeprops=dict(width=0.3))
circle = plt.Circle((0,0),0.70,fc='white')
ax.add_artist(circle)
ax.set_title('Government & Public Policy Overview - 2023')
ax.legend(data_labels, loc="best")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_16.png')
plt.clf()