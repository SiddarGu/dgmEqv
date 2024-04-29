
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

data_labels = ["Crop Yield", "Food Safety", "Waste Management", "Soil Quality", "Logistics"]
data = [17, 25, 6, 15, 37]
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%1.1f%%', textprops={'color':"w"})
circle = plt.Circle((0,0), 0.75, color='white')
ax.add_artist(circle)

ax.set_title('Agro-Production Trends - 2023')
ax.legend(data_labels, loc='lower right')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_108.png')
plt.clf()