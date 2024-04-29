
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

data_labels = ["Prevention Awareness","Health Education","Vaccination Rate","Treatment Access","Disease Control"]
data = [44,14,21,15,6]
line_labels = ["Category","ratio"]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90,counterclock=False,radius=1.2,colors=['#F7A259','#F6D95F','#B2D4F0','#F27D9F','#71B9A2'])
circle = Circle(xy=(0,0),radius=0.7,color='white')
ax.add_artist(circle)
ax.legend(data_labels,loc='center', bbox_to_anchor=(1.1, 0.75))
ax.set_title("Healthcare and Health - 2021 Outlook", fontsize=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_125.png')
plt.clf()