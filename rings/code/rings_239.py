
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Education","Infrastructure","Public Services","Security","Economy"]
data = [25,20,30,18,7]
line_labels = ["Sector","Ratio"]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()
ax.pie(data, labels=data_labels, autopct="%1.1f%%", startangle=90, counterclock=False, colors = ['b','y','g','r','m'])
my_circle=plt.Circle( (0,0), 0.7, color='white')
ax.add_artist(my_circle)
ax.legend(data_labels, loc="upper right")
plt.title("Government and Public Policy Impact - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_15.png")
plt.clf()