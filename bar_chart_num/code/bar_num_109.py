
import numpy as np
import matplotlib.pyplot as plt

years = [2018,2019,2020,2021]
Psychology = [200,210,220,230]
Sociology = [150,170,190,210]
Anthropology = [100,120,140,160]

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111)

ax.set_title('Number of publications in Social Sciences and Humanities from 2018 to 2021')

bar_width = 0.2

bars1 = ax.bar(np.array(years)-bar_width,Psychology,width=bar_width,align='center',label='Psychology',color='#1f77b4')
bars2 = ax.bar(np.array(years),Sociology,width=bar_width,align='center',label='Sociology',color='#ff7f0e')
bars3 = ax.bar(np.array(years)+bar_width,Anthropology,width=bar_width,align='center',label='Anthropology',color='#2ca02c')

ax.set_xticks(years)

ax.set_ylabel('Number of Publications')
ax.set_xlabel('Years')

ax.legend()

for bar1, bar2,bar3 in zip(bars1, bars2,bars3):
    ax.annotate("%.0f" % bar1.get_height(),
                xy=(bar1.get_x() + bar1.get_width() / 2, bar1.get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate("%.0f" % bar2.get_height(),
                xy=(bar2.get_x() + bar2.get_width() / 2, bar2.get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate("%.0f" % bar3.get_height(),
                xy=(bar3.get_x() + bar3.get_width() / 2, bar3.get_height()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig(r'Bar Chart\png\555.png')
plt.clf()