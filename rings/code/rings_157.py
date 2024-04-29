
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data_labels = ['Law Compliance','Public Opinion','Social Welfare','Infrastructure']
data = [25,17,22,36]
line_labels = ['Category']

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_title("Government Performance Indicators-2023")

ax.pie(data, labels = data_labels, startangle=90, counterclock=False, 
        autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.1)

centre_circle = plt.Circle((0,0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.tight_layout()
ax.legend(data_labels, loc="upper right", bbox_to_anchor=(1, 0.5))
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_123.png')
plt.clf()