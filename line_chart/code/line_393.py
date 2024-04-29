
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,2,4,6,8,10,12])
y = np.array([20,25,30,35,40,45,50])

fig = plt.figure(figsize=(8,6))
ax = plt.subplot()

ax.plot(x, y, label='Temperature (degrees)', color='#00A2E8', marker='o')
ax.set_title('Temperature change in a chemical reaction experiment')
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Temperature (degrees)')
ax.set_xticks(x)
ax.legend(loc='best')

plt.tight_layout()
plt.savefig('line chart/png/297.png')
plt.clf()