
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Home Prices","Rental Rates","Vacancy Rates","Building Permits","Property Taxes"]
data = [30,20,13,14,23]
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, colors=colors)
circle = plt.Circle((0,0), 0.70, color='white')
ax.add_artist(circle)

ax.legend(data_labels, loc="upper left", bbox_to_anchor=(1,0.8))
ax.set_title("Real Estate and Housing Market - 2023")

plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_49.png")
plt.clf()