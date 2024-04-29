
import matplotlib.pyplot as plt
import numpy as np

#create data
data = np.array([[60,2.5],[63,2.8],[72,3.2],[68,2.9],[71,3.3],[77,3.7],[83,4.2],[81,4.1],[73,3.5],[69,3.2],[65,2.7],[62,2.6]])
months = np.array(['January','February','March','April','May','June','July','August','September','October','November','December'])

#create figure
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(111)

#plot lines
ax.plot(months,data[:,0],label="Hotel Occupancy Rate(%)")
ax.plot(months,data[:,1],label="Airline Passengers(million)")

#set x ticks
plt.xticks(np.arange(12),months,rotation=45)

#annotate
for x,y in zip(months,data[:,0]):
    ax.annotate('%.2f'%y,(x,y+0.05))
for x,y in zip(months,data[:,1]):
    ax.annotate('%.2f'%y,(x,y+0.05))

#set legend
ax.legend(loc='upper left',frameon=False)

#set title
ax.set_title('Tourist traffic in a popular tourist city in 2020')

#tight_layout
plt.tight_layout()

#save image
plt.savefig('./line chart/png/605.png')

#clear figure
plt.clf()