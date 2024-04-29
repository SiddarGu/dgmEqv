
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data_labels = ["Profit","Expenses","Investments","Revenue","Market Share"]
line_labels = ["Category"]
data = np.array([[43,20,17,13,7]])

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(data[0], startangle=90, counterclock=False, autopct='%.2f%%', colors=['#5c4dff','#d6ebfe','#a6c2ff','#87b3ff','#ffb4b8'])
circle = mpatches.Circle((0,0), 0.6, color='white')
ax.add_artist(circle)
ax.set_title("Financial Performance - 2023")
ax.legend(data_labels, loc="best")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_55.png')
plt.close()