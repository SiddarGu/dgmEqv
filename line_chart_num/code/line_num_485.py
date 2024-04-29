
import matplotlib.pyplot as plt
import numpy as np

#create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

#plot data
x = np.array([2001, 2002, 2003, 2004])
y1 = np.array([500, 600, 400, 800])
y2 = np.array([800, 900, 1100, 1300])
y3 = np.array([1000, 1100, 1200, 1500])

ax.plot(x, y1, color='green', marker='o',label='Crop A(tonnes)')
ax.plot(x, y2, color='red', marker='o',label='Crop B(tonnes)')
ax.plot(x, y3, color='blue', marker='o',label='Crop C(tonnes)')

#title
ax.set_title('Harvest of three main crops in the US from 2001 to 2004')

#x-axis label
ax.set_xlabel('Year')

#y-axis label
ax.set_ylabel('tonnes')

#xticks
ax.set_xticks(x)

#legend
ax.legend(loc='best')

#annotate
for i,j in zip(x,y1):
    ax.annotate(str(j),xy=(i,j),rotation=45)

for i,j in zip(x,y2):
    ax.annotate(str(j),xy=(i,j),rotation=45)

for i,j in zip(x,y3):
    ax.annotate(str(j),xy=(i,j),rotation=45)

#resize
plt.tight_layout()

#save
plt.savefig('line chart/png/299.png')

#clear
plt.clf()