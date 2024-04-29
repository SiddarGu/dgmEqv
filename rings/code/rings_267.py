
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Education", "Arts", "Ethics", "Sociology", "Psychology"]
data = [0.38, 0.17, 0.1, 0.25, 0.1]
line_labels = ["Topic", "ratio"]

fig, ax = plt.subplots(figsize=(8,6))
ax.set_title("Social Sciences and Humanities - 2023")
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%1.1f%%', pctdistance=0.8)
circle = plt.Circle((0,0), 0.5, color="white")
ax.add_artist(circle)
ax.legend(data_labels, loc="lower left")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_124.png', dpi=300)
plt.clf()