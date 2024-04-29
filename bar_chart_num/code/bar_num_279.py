
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10,8))
Energy = [100,200,300,400]
Computers = [1,2,3,4]
Satellites = [0.2,0.4,0.6,0.8]
x = np.arange(len(Energy))
width = 0.25
rects1 = ax.bar(x - width, Energy, width, label='Energy(kW)')
rects2 = ax.bar(x, Computers, width, label='Computers(million)')
rects3 = ax.bar(x + width, Satellites, width, label='Satellites(million)')

ax.set_ylabel('Output')
ax.set_title('Energy, Computer and Satellite Output from 2015 to 2018')
ax.set_xticks(x)
ax.set_xticklabels(('2015', '2016', '2017', '2018'))
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=0, wrap=True)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()
plt.savefig('Bar Chart/png/457.png', dpi=300)
plt.clf()