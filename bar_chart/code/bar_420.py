
import matplotlib.pyplot as plt

transport = ['Road','Rail','Air']
cost = [0.2, 0.3, 1.5]
time = [15, 10, 5]

fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot()
ax.bar(transport, cost, bottom=0, width=0.25, label='Cost/km(USD)') 
ax.bar(transport, time, bottom=0, width=0.25, label='Time(minutes)')
ax.set_xticks(transport)
plt.title('Cost and time of transportation by different modes of transport in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/384.png')
plt.clf()