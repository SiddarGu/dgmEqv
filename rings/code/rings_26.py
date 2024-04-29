
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

data_labels = ["Disease Prevention", "Vaccine Administration", "Healthcare Accessibility", "Treatment Quality", "Patients' Awareness"]
data = [35, 20, 25, 10, 10]
line_labels = ["Category", "ratio"]

mpl.rcParams["font.size"] = "12"
mpl.rcParams["font.family"] = "Arial"
fig = plt.figure(figsize=(10,10)) 
ax = fig.add_subplot(111)
ax.pie(data, colors=['red', 'orange', 'yellow', 'green', 'blue'], startangle=90, counterclock=False)
ax.set_title("Healthcare Impact Assessment - 2023")
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
ax.legend(data_labels, loc="center left", bbox_to_anchor=(1.2, 0.5))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_37.png')
plt.clf()