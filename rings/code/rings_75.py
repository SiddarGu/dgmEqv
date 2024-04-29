
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_labels = ['Online Sales','Store Sales','Returns','Delivery Efficiency','Customer Satisfaction']
data = np.array([44,32,11,9,4])
line_labels = ['Category','ratio']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%', pctdistance=0.8)

plt.Circle((0,0),0.5, color='white')
ax.add_artist(plt.Circle((0,0),0.5, color='white'))
ax.legend(data_labels, loc="upper left")
plt.title("Retail & E-commerce Performance in 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_143.png')
plt.clf()