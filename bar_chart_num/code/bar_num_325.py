
import matplotlib.pyplot as plt
import numpy as np 

data = [['USA',50,100,60],
        ['UK',60,90,70],
        ['Germany',70,80,80],
        ['France',80,70,90]]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)

labels = [i[0] for i in data]
museums = [i[1] for i in data]
galleries = [i[2] for i in data]
theatres = [i[3] for i in data]

x = np.arange(len(labels))
width = 0.2

rects1 = ax.bar(x, museums, width, color='r', label='Museums')
rects2 = ax.bar(x + width, galleries, width, color='b', label='Galleries')
rects3 = ax.bar(x + width + width, theatres, width, color='g', label='Theatres')

ax.set_xticks(x + width)
ax.set_xticklabels(labels)
ax.legend(loc = 'upper left')

plt.title('Number of Arts and Culture Venues in Four Countries in 2021')

for rect in rects1 + rects2 + rects3:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width()/2, height/2),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/432.png')
plt.clf()