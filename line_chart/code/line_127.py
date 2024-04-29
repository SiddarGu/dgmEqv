
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,6))
ax=plt.subplot()
data = np.array([[2020,800,700],[2021,900,800],[2022,1000,900],[2023,1100,1000],[2024,1200,1100]])
x = data[:,0]
y1 = data[:,1]
y2 = data[:,2]
ax.plot(x, y1, label='Tax Revenue (billion dollars)', color='b')
ax.plot(x, y2, label='Expenditure (billion dollars)', color='r')
plt.xticks(x)
plt.title('Government Tax Revenue and Expenditure from 2020 to 2024')
plt.legend(loc='upper left')
ax.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/491.png')
plt.clf()