
import matplotlib.pyplot as plt
import numpy as np

V = [0.5, 1.0, 1.5, 2.0, 2.5] 
A = [0.1, 0.2, 0.3, 0.4, 0.5]
R = [5, 2.5, 1.67, 1.25, 1]

plt.figure(figsize=(9, 7))
ax = plt.subplot()
ax.plot(V, A, color='green', marker='o', label='Current Vs Voltage')
ax.plot(V, R, color='blue', marker='s', label='Resistance Vs Voltage')

ax.set_xlabel('Voltage (V)', fontsize=14)
ax.set_ylabel('Current (A) & Resistance (ohm)', fontsize=14)
ax.set_title('Voltage, current, and resistance relationship in a circuit', fontsize=16)
ax.grid(True, linestyle='-.', linewidth=0.2)
ax.annotate('5', (0.5, 0.1))
ax.annotate('2.5', (1.0, 0.2))
ax.annotate('1.67', (1.5, 0.3))
ax.annotate('1.25', (2.0, 0.4))
ax.annotate('1', (2.5, 0.5))

ax.legend(loc='upper left', fontsize=12)
plt.xticks(V)
plt.tight_layout()
plt.savefig(r'line chart/png/158.png')
plt.clf()