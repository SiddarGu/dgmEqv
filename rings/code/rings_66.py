
import matplotlib.pyplot as plt 
import numpy as np

data_labels = ["Education","Cultural Development","Human Development","Economic Development","Social Development"]
data = [37,25,18,13,7]
line_labels = ["Category","ratio"]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['red','orange','yellow','green','blue'])
ax.add_artist(plt.Circle((0,0),0.7,color='white'))
ax.legend(data_labels)
ax.set_title("Social Sciences and Humanities Indicators - 2023")
plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_134.png')
plt.clf()