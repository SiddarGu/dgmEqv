
import matplotlib.pyplot as plt
import numpy as np

Region = ['East', 'South', 'West', 'North']
Hospitals = [15, 20, 25, 30]
Doctors = [100, 150, 120, 180]
Nurses = [250, 300, 270, 340]

x = np.arange(len(Region)) 
width = 0.2

fig, ax = plt.subplots(figsize=(9, 6))
rects1 = ax.bar(x - width, Hospitals, width, label='Hospitals')
rects2 = ax.bar(x, Doctors, width, label='Doctors')
rects3 = ax.bar(x + width, Nurses, width, label='Nurses')

ax.set_title('Healthcare resources in four regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Region)
ax.legend(loc='upper left')

for rect in rects1 + rects2 + rects3:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/156.png')
plt.clf()