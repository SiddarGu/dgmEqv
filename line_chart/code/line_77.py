
import matplotlib.pyplot as plt
import numpy as np

month = ['January','February','March','April','May']
order_A = [50,60,65,70,55]
order_B = [35,40,45,50,45]
order_C = [45,50,55,60,70]
order_D = [60,70,75,80,90]

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(1,1,1)
plt.plot(month,order_A, label='Order A')
plt.plot(month,order_B, label='Order B')
plt.plot(month,order_C, label='Order C')
plt.plot(month,order_D, label='Order D')
plt.xticks(rotation=45)
plt.legend(loc='best')
plt.title('Changes in orders of four different products in 2021')
plt.tight_layout()
plt.savefig('line chart/png/462.png')
plt.clf()