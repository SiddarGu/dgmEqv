
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y1 = np.array([13,17,11,13,15])
y2 = np.array([1020,1022,1018,1025,1022])
y3 = np.array([50,45,60,55,52])
y4 = np.array([3.5,2.4,4.4,3.2,1.8])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.plot(x,y1,color='b',label='Wind Speed(km/h)')
ax.plot(x,y2,color='r',label='Air Pressure(hPa)')
ax.plot(x,y3,color='g',label='Humidity(%)')
ax.plot(x,y4,color='y',label='Rainfall(mm)')
ax.set_title('Average Weather Conditions in June in San Francisco, California',fontsize=14)
ax.set_xlabel('Month')
ax.set_xticks(x)
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
plt.savefig('line chart/png/419.png')
plt.cla()