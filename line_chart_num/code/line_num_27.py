
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 1000, 800, 200],
        ['UK', 900, 600, 300],
        ['France', 800, 400, 500],
        ['Germany', 500, 400, 600]]

labels, y1, y2, y3 = zip(*data)
x = np.arange(len(labels))
width = 0.2

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

rects1 = ax.bar(x-width, y1, width, color='#3399ff', label='Museums')
rects2 = ax.bar(x, y2, width, color='#ff9900', label='Galleries')
rects3 = ax.bar(x+width, y3, width, color='#00cc00', label='Festivals')

ax.set_title('Arts and Culture Landscape in Europe', fontsize=20)
ax.set_xlabel('Country')
ax.set_ylabel('Number')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='upper right')

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
plt.savefig('line chart/png/214.png')
plt.clf()