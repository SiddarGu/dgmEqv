
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Performance Evaluation', 'Talent Acquisition', 'Workplace Environment', 'Training & Development', 'Productivity']
data = [25, 23, 14, 22, 16]
line_labels = ['Category','ratio']

fig, ax = plt.subplots(figsize=(12,8))
explode = np.zeros(len(data_labels))
explode[0] = 0.1
wedges, texts, autotexts = ax.pie(data, explode=explode, counterclock=False, startangle=90, autopct='%.0f%%')
ax.set_title("Human Resources Management Trends - 2021")
ax.legend(data_labels, loc="upper left")
centre_circle = plt.Circle((0,0), 0.6, color='white', fc='white',linewidth=0)
ax.add_artist(centre_circle)
plt.setp(autotexts, size=15, weight="bold")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_36.png')
plt.clf()