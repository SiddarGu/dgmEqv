
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
data = np.array([[20, 450, 910], 
                 [15, 400, 850], 
                 [25, 500, 1000], 
                 [10, 250, 660]])
region_name = ["North America", "South America", "Europe", "Africa"]
hospitals = data[:, 0]
doctors = data[:, 1]
nurses = data[:, 2]

x = np.arange(len(region_name))
width = 0.2

rects1 = ax.bar(x - width, hospitals, width=width, label="Hospitals")
rects2 = ax.bar(x, doctors, width=width, label="Doctors")
rects3 = ax.bar(x + width, nurses, width=width, label="Nurses")

ax.set_ylabel('Number')
ax.set_title('Healthcare services in four regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(region_name)
plt.legend(loc="upper left")

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.tight_layout()
plt.savefig('Bar Chart/png/602.png')
plt.clf()