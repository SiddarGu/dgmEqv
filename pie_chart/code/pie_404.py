
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 8))
# Plot pie chart
ax = fig.add_subplot(111)
regions = ['North America', 'Europe', 'Africa', 'Asia', 'South America', 'Oceania']
share = [20, 30, 10, 25, 10, 5]
ax.pie(share, labels=regions, autopct='%.2f%%', startangle=90)
# set legend
ax.legend(regions, loc="best", bbox_to_anchor=(1, 0.5))
# set title
ax.set_title('Global Tourism Share in 2023')
# set x y label name
ax.set_xlabel('Regions')
ax.set_ylabel('Tourism Share')
# set font
plt.rcParams['font.sans-serif'] = 'SimHei'
# set tight_layout
plt.tight_layout()
# save figure
plt.savefig('pie chart/png/448.png')
# clear current image state
plt.cla()