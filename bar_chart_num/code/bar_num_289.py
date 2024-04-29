
import matplotlib.pyplot as plt
import numpy as np

# construct data
Country = np.array(['USA','UK','Germany','France'])
Museums = np.array([50,60,70,80])
Galleries = np.array([400,500,450,420])
Theatres = np.array([300,200,250,220])

# create figure 
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# plot data
x = np.arange(len(Country))
ax.bar(x, Museums, bottom=Galleries+Theatres,label='Museums',width=0.4,color='#FFC300')
ax.bar(x, Galleries, bottom=Theatres,label='Galleries',width=0.4,color='#FF5733')
ax.bar(x, Theatres,label='Theatres',width=0.4,color='#C70039')

# set x axis
ax.set_xticks(x)
ax.set_xticklabels(Country)

# set title and legend
ax.set_title('Number of museums, galleries and theatres in four countries in 2021')
ax.legend(loc='upper left')

# annotate value of each data point for every variables
for x_i,y_i in zip(x,Museums):
    ax.annotate(str(y_i),xy=(x_i,y_i),xytext=(0,5),textcoords='offset points',ha='center')
for x_i,y_i in zip(x,Galleries):
    ax.annotate(str(y_i),xy=(x_i,y_i),xytext=(0,5),textcoords='offset points',ha='center')
for x_i,y_i in zip(x,Theatres):
    ax.annotate(str(y_i),xy=(x_i,y_i),xytext=(0,5),textcoords='offset points',ha='center')

# adjust figure size
plt.tight_layout()

# save figure
plt.savefig('Bar Chart/png/345.png',dpi=300)

# clear current image state
plt.clf()