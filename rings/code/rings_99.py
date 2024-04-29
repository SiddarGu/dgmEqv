
import matplotlib.pyplot as plt
import numpy as np

#transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Art", "Music", "Theater", "Literature", "Media"]
data = [0.36, 0.29, 0.13, 0.12, 0.10]
line_labels = ["Category", "ratio"]

#plot the data with the type of rings chart
fig, ax = plt.subplots(figsize=(6,6))
ax.pie(data, startangle=90,counterclock=False, colors=['#f07c6c','#f1ca50','#b4e2fa','#9bd3b2','#aed4f7'])
centre_circle = plt.Circle((0,0), 0.70, fc='white')
ax.add_artist(centre_circle)
ax.set_title("Arts and Culture - A Comprehensive Overview")
ax.legend(data_labels, bbox_to_anchor=(1, 0.5), loc="center left")
plt.tight_layout()
plt.savefig(r"/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_46.png")
plt.clf()