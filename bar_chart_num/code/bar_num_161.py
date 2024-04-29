
import matplotlib.pyplot as plt
import numpy as np

#create figure
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)

#data
Country = ('USA','UK','Germany','France')
Literature = (1200,900,1500,1100)
Music = (800,650,900,750)
Theater = (450,350,550,400)

#plot
bar_width =0.2
ax.bar(Country, Literature, width=bar_width, label='Literature')
ax.bar(np.arange(len(Country))+bar_width, Music, width=bar_width, label='Music')
ax.bar(np.arange(len(Country))+2*bar_width, Theater, width=bar_width, label='Theater')

#add title, labels and legend
plt.title('Number of social science and humanities works in four countries in 2021')
ax.set_xticks(np.arange(len(Country))+bar_width)
ax.set_xticklabels(Country)
ax.set_ylabel('Number of Works')
ax.legend(bbox_to_anchor=(1, 1))

#annotate
for x,y in enumerate(Literature):
    ax.annotate(y, xy=(x-bar_width/2,y+50), xytext=(0,3), textcoords='offset points', ha='center', va='bottom')
for x,y in enumerate(Music):
    ax.annotate(y, xy=(x+bar_width/2,y+50), xytext=(0,3), textcoords='offset points', ha='center', va='bottom')
for x,y in enumerate(Theater):
    ax.annotate(y, xy=(x+3*bar_width/2,y+50), xytext=(0,3), textcoords='offset points', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/581.png')
plt.clf()