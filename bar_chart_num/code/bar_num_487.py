

import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot(111) 
ax.bar(['USA','UK','Germany','France'], [250,400,300,350], label='Hotel Rooms', width=0.4, color='#ffe7ac') 
ax.bar(['USA','UK','Germany','France'], [450,500,400,470], label='Tourists', width=0.4, bottom=[250,400,300,350], color='#f4a742') 
ax.set_title("Number of hotel rooms and tourists in four countries in 2021") 
ax.set_xlabel('Country') 
ax.set_ylabel('Number') 
ax.legend()
for x, y, label in zip(['USA','UK','Germany','France'], [650,900,700,820], [250,400,300,350]):
    ax.annotate('{}'.format(y-label), xy=(x, y-label/2), xytext=(0,3), textcoords="offset points", ha='center', va='bottom')
plt.xticks(['USA','UK','Germany','France'], ['USA','UK','Germany','France'], rotation=45)
plt.tight_layout()
plt.savefig('Bar Chart/png/5.png')
plt.clf()