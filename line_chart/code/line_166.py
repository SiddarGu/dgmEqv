
import matplotlib.pyplot as plt
import numpy as np

x = np.array(['January','February','March','April','May','June','July','August','September','October','November','December'])
y1 = np.array([25,27,30,32,35,38,40,45,50,55,60,65])
y2 = np.array([3,4,6,8,10,12,14,16,18,20,22,24])
y3 = np.array([20,22,18,15,12,10,8,5,3,2,1,2])
y4 = np.array([30,32,35,38,40,45,50,55,60,65,70,75])

fig = plt.figure(figsize=(15,8))
ax1 = fig.add_subplot(111)

ax1.plot(x, y1, label='Wind Energy(GW)')
ax1.plot(x, y2, label='Solar Energy(GW)')
ax1.plot(x, y3, label='Nuclear Energy(GW)')
ax1.plot(x, y4, label='Hydroelectric Energy(GW)')

plt.xticks(x, x, rotation=45)
ax1.set_title('Renewable energy sources trend in Germany in 2021')
ax1.set_xlabel('Month')
ax1.set_ylabel('Energy(GW)')
ax1.legend(loc='upper left')
plt.tight_layout()

plt.savefig("line chart/png/198.png")
plt.clf()