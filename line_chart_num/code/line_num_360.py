
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y1 = np.array([200, 250, 300, 350, 400, 450, 500, 550])
y2 = np.array([300, 350, 400, 450, 500, 550, 600, 650])

plt.figure(figsize=(10, 6))
ax = plt.subplot()
ax.set_xticks(x)
ax.set_xticklabels(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'])

plt.plot(x, y1, label='Online Purchases', color='red')
plt.plot(x, y2, label='Retail Purchases', color='blue')
plt.title('Comparison of Online and Retail Purchases in 2021')
plt.xlabel('Month')
plt.ylabel('Purchases(million dollars)')

for i, txt in enumerate(y1):
    ax.annotate(txt, (x[i], y1[i]))

for i, txt in enumerate(y2):
    ax.annotate(txt, (x[i], y2[i]))

plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/366.png')
plt.clf()