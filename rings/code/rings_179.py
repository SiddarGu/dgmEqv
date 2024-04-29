
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Customer Reach","Advertising","Logistic","Delivery","Product Quality"]
data = [30,15,25,15,15]
line_labels = ["Category","ratio"]

fig,ax = plt.subplots(figsize=(9, 6))
ax.set_title("E-commerce Performance in Retail - 2023")

ax.pie(data,labels=data_labels,startangle=90,counterclock=False)
circle = plt.Circle((0,0),0.7,color="white")
ax.add_artist(circle) 
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(-0.1, 1.))
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_22.png")
plt.clf()