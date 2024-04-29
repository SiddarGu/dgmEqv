
import matplotlib.pyplot as plt
import numpy as np

month = ['January','February','March','April','May','June','July','August']
windSpeed = [5,6,7,8,9,10,12,15]
humidity = [45,35,25,20,15,10,5,2]

plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.plot(month,windSpeed,linestyle='-',marker='o',color='b',label='Wind Speed (m/s)')
ax.plot(month,humidity,linestyle='-',marker='o',color='r',label='Humidity (%)')
ax.set_title('Change in Wind Speed and Humidity over a year in San Francisco')
ax.legend(loc='best',fontsize='x-large')
plt.xticks(np.arange(8),month,rotation=20)
plt.tight_layout()
plt.savefig('line chart/png/357.png')
plt.clf()