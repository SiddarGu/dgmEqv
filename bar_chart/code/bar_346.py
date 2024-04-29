
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
labels = ['Basketball', 'Football', 'Rugby', 'Hockey']
Attendance = [21000, 30000, 25000, 15000]
Prize_Money = [2.5, 4.5, 3.5, 2]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10,7))
rects1 = ax.bar(x - width/2, Attendance, width, label='Average Attendance', color='skyblue')
rects2 = ax.bar(x + width/2, Prize_Money, width, label='Prize Money (Million)', color='steelblue')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number')
ax.set_title('Average attendance and Prize money for four major sports in 2021')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=25, ha="right", va="top", multialignment="center")
ax.legend(bbox_to_anchor=(1, 1), loc='upper left')

plt.tight_layout()
fig.savefig('bar chart/png/86.png')
plt.clf()