
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ['Spending','Regulation','Taxation','Law Enforcement','Education']
data = np.array([27, 23, 25, 15, 10])
line_labels = ['Category', 'ratio']

plt.figure(figsize=(8,8))
ax = plt.subplot()
ax.pie(data, startangle=90, counterclock=False, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
circle = mpatches.Circle( (0,0), 0.75, color='white')
ax.add_artist(circle)
plt.legend(data_labels, loc="upper left")
plt.title("Public Policy Impact - 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_57.png')
plt.clf()