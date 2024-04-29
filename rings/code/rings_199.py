
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Food Quality","Service Quality","Product Availability","Cost Management","Hygiene Standards"]
data = [26,17,14,14,29]
line_labels = ["Category","ratio"]

fig, ax = plt.subplots(figsize=(9,7))
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#99b898', '#feceab', '#e84a5f', '#fa8231', '#2a363b'])
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)
plt.legend(data_labels)
ax.set_title("Food and Beverage Industry Performance - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_52.png")
plt.clf()