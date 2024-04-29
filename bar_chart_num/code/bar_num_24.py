
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 7))

Country = ['USA','UK','Germany','France']
Tickets_Sold = [200, 150, 180, 230]
Viewers = [450, 400, 350, 300]

x = np.arange(len(Country))
width = 0.35

ax = fig.add_subplot()
ax.bar(x - width/2, Tickets_Sold, width, label='Tickets Sold(million)')
ax.bar(x + width/2, Viewers, width, label='Viewers(million)')

ax.set_title('Number of tickets sold and viewers in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend()

ax.annotate('{}'.format(Tickets_Sold[0]), xy=(x[0] - width/2, Tickets_Sold[0]), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
ax.annotate('{}'.format(Tickets_Sold[1]), xy=(x[1] - width/2, Tickets_Sold[1]), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
ax.annotate('{}'.format(Tickets_Sold[2]), xy=(x[2] - width/2, Tickets_Sold[2]), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
ax.annotate('{}'.format(Tickets_Sold[3]), xy=(x[3] - width/2, Tickets_Sold[3]), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

ax.annotate('{}'.format(Viewers[0]), xy=(x[0] + width/2, Viewers[0]), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
ax.annotate('{}'.format(Viewers[1]), xy=(x[1] + width/2, Viewers[1]), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
ax.annotate('{}'.format(Viewers[2]), xy=(x[2] + width/2, Viewers[2]), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
ax.annotate('{}'.format(Viewers[3]), xy=(x[3] + width/2, Viewers[3]), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/386.png', bbox_inches='tight')
plt.clf()