
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

region = ["North America","Europe","South America","Africa"]
donations = [20, 15, 10, 5]
volunteers = [4500, 3000, 2000, 1000]

bar1 = ax.bar(region, donations, label="Donations (million)", bottom=0)
bar2 = ax.bar(region, volunteers, bottom=donations, label="Volunteers")

ax.set_title("Donations and volunteer count in four regions in 2021")
ax.set_xlabel("Region")
ax.set_ylabel("Count")
ax.legend(loc=2)

ax.set_xticks(region)
ax.grid(True)

for bar1, bar2 in zip(bar1, bar2):
    y1 = bar1.get_height()
    y2 = bar2.get_height()
    ax.annotate('{}'.format(y1), xy=(bar1.get_x() + bar1.get_width()/2, y1/2), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', rotation=90)
    ax.annotate('{}'.format(y2), xy=(bar2.get_x() + bar2.get_width()/2, y1+y2/2), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', rotation=90)

plt.tight_layout()
plt.savefig('Bar Chart/png/494.png')
plt.clf()