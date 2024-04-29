
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Vaccination Rate','Health Insurance Coverage','Healthcare Quality','Hygiene Standards']
data = np.array([[31, 39, 14, 16]])
line_labels = ['Category']

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Healthcare System Performance Overview - 2023")

ax.pie(data[0], labels=data_labels, startangle=90, counterclock=False)

centre_circle = plt.Circle((0,0), 0.75, color='white', fc='white', linewidth=0)
ax.add_artist(centre_circle)
ax.legend(data_labels, loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_46.png')
plt.clf()