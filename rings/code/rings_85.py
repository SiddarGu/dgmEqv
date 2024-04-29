
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Arts', 'Language', 'History', 'Human Geography', 'Social Sciences'] 
data = [13, 6, 20, 25, 36]
line_labels = np.arange(len(data))

fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(data, startangle=90, counterclock=False)
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc="upper left")
ax.set_title('Social Science and Humanities - 2023', fontsize=15)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_24.png')
plt.clf()