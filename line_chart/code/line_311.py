
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
y = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

ax.set_title('Voltage increase in a circuit over 90 minutes')
ax.set_xlabel('Time (minutes)')
ax.set_ylabel('Voltage (volts)')

ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())

ax.plot(x, y, color='royalblue', linestyle='-', linewidth=2, marker='o')

plt.tight_layout()
plt.savefig('line chart/png/281.png')
plt.clf()