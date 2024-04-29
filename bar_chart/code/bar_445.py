
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
data = [[5000, 1000], [3500, 900], [3000, 800], [4500, 1100]]

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()
bar_width = 0.35

rects1 = ax.bar(x - bar_width/2, [i[0] for i in data], bar_width, label='Lawyers')
rects2 = ax.bar(x + bar_width/2, [i[1] for i in data], bar_width, label='Judges')

ax.set_xticks(x)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'], rotation=45, ha='right', wrap=True)
ax.set_title('Number of lawyers and judges in four countries in 2021')
ax.set_ylabel('Number')
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/29.png')
plt.clf()