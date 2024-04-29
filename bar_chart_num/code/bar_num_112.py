
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
width = 0.2

Fig = plt.figure(figsize=(10,6))
ax = Fig.add_subplot(111)
ax.bar(x, [400, 450, 480, 420], width, label='Cafes')
ax.bar(x+width, [500, 550, 580, 520], width, label='Bakeries')
ax.bar(x+width*2, [600, 650, 700, 620], width, label='Restaurants')
ax.set_xticks(x+width/2)
ax.set_xticklabels(['North America', 'Europe', 'Asia', 'South America'])
ax.set_title('Number of food and beverage outlets in four regions in 2021')
ax.legend()
ax.annotate('{}'.format(400), xy=(x[0], 400), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(450), xy=(x[1], 450), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(480), xy=(x[2], 480), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(420), xy=(x[3], 420), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(500), xy=(x[0]+width, 500), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(550), xy=(x[1]+width, 550), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(580), xy=(x[2]+width, 580), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(520), xy=(x[3]+width, 520), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(600), xy=(x[0]+width*2, 600), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(650), xy=(x[1]+width*2, 650), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(700), xy=(x[2]+width*2, 700), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
ax.annotate('{}'.format(620), xy=(x[3]+width*2, 620), xytext=(0, 10), 
            textcoords="offset points",
            ha='center', va='bottom')
plt.tight_layout()
plt.savefig('Bar Chart/png/330.png')
plt.clf()