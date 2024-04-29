
import matplotlib.pyplot as plt
import numpy as np

#set figure size
plt.figure(figsize=(8,8))

#create a subplot
ax = plt.axes()

#set data
labels = ['Solar Energy','Wind Energy','Hydro Energy','Geothermal Energy','Biomass Energy']
sizes = [25, 20, 30, 15, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6']

#plot data
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90,shadow=True,textprops={'fontsize': 14})

#set title
ax.set_title('Distribution of Renewable Energy Sources in the USA, 2023',fontsize=20)

#tight layout
plt.tight_layout()

#save figure
plt.savefig('pie chart/png/277.png')

#clear the current image state
plt.cla()