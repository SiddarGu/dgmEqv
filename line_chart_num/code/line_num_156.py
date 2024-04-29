
import matplotlib.pyplot as plt

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
shipments = [100, 120, 110, 90, 130, 140, 150, 160]
time = [4, 3.5, 4.2, 3.7, 4.5, 3.8, 4.1, 4.3]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(month, shipments, color='g', label='Number of Shipments')
ax.plot(month, time, color='b', label='Average Delivery Time(days)')

for a,b in zip(month, shipments):
    ax.text(a, b, b, ha='center', va='bottom', fontsize=10)
for c,d in zip(month, time):
    ax.text(c, d, d, ha='center', va='bottom', fontsize=10)

ax.legend(loc='best')
ax.set_xlabel('Month')
ax.set_title('Monthly number of shipments and average delivery time in year 2021')
plt.xticks(month, rotation=90, wrap=True)
plt.tight_layout()
plt.savefig('line chart/png/584.png')
plt.clf()