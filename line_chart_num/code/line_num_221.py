
import matplotlib.pyplot as plt 
voltage, current, power = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0], [0.2, 0.4, 0.6, 0.8, 1.0, 1.2], [0.1, 0.4, 0.9, 1.6, 2.5, 3.6]

plt.figure(figsize=(10,7))
plt.plot(voltage, current, color='g', linestyle='-', marker='o', label='Current')
plt.plot(voltage, power, color='r', linestyle='-', marker='o', label='Power')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A) and Power (W)')
plt.title('Voltage, Current, and Power Relationship in a Circuit')
plt.legend(loc='upper left')

for a, b, c in zip(voltage, current, power):
    plt.annotate(f'({a}, {b})', xy=(a, b), xytext=(a-0.15, b-0.1))
    plt.annotate(f'({a}, {c})', xy=(a, c), xytext=(a+0.1, c+0.1))
plt.xticks(voltage)
plt.tight_layout()
plt.savefig('line chart/png/31.png')
plt.close()