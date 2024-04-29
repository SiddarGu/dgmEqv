
import matplotlib.pyplot as plt
import numpy as np
data_labels = ["Music","Theatre","Visual Arts","Literature","Heritage"]
data = [0.29, 0.15, 0.25, 0.16, 0.15]
line_labels = ["Category","ratio"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#00A7D7','#01BFBF','#BFE2FF','#77B7FF','#B2FFFD'])
inner_circle = plt.Circle((0,0), 0.4, color='white')
ax.add_artist(inner_circle)
ax.set_title("Cultural Diversity - 2023")
ax.legend(data_labels, loc="upper left", bbox_to_anchor=(1, 0, 0.25, 1))
plt.grid(axis='y', linestyle='--', color='grey', linewidth=0.3)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_14.png')
plt.close(fig)