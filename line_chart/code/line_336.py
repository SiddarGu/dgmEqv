
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
Month = ['January', 'February', 'March', 'April', 'May']
Production_A = [10000, 12000, 14000, 13000, 15000]
Production_B = [8000, 7000, 8000, 9000, 11000]
Production_C = [5000, 6000, 7000, 8000, 9000]

plt.figure(figsize=(10,6))
plt.plot(x, Production_A, label='Production A', marker='o')
plt.plot(x, Production_B, label='Production B', marker='*')
plt.plot(x, Production_C, label='Production C', marker='^')
plt.xticks(x, Month, rotation=45, wrap=True)
plt.title('Output of three types of production in a factory from January to May')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/377.png')
plt.clf()