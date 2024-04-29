
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))

x=np.arange(2020,2024)
y1=np.array([1000,1100,1200,1500])
y2=np.array([800,900,1100,1300])
y3=np.array([1200,1400,1500,1600])
y4=np.array([500,700,900,1200])

plt.plot(x,y1,label='Cereal Yield(metric tonnes)')
plt.plot(x,y2,label='Vegetable Yield(metric tonnes)')
plt.plot(x,y3,label='Fruit Yield(metric tonnes)')
plt.plot(x,y4,label='Animal Yield')

plt.xticks(x,('2020','2021','2022','2023'))
plt.title('Yield of Agriculture Products in the US from 2020 to 2023')
plt.xlabel('Year')
plt.ylabel('Yield')
plt.legend(loc='best')
plt.tight_layout()

plt.savefig('line chart/png/456.png')
plt.clf()