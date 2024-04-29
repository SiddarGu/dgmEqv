
import matplotlib.pyplot as plt

labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
Hotel_A = [90, 85, 80, 75, 85, 90, 95, 90]
Hotel_B = [80, 75, 70, 65, 75, 80, 85, 80]
Hotel_C = [60, 65, 70, 75, 80, 85, 90, 85]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

ax.plot(labels, Hotel_A, label='Hotel A')
ax.plot(labels, Hotel_B, label='Hotel B')
ax.plot(labels, Hotel_C, label='Hotel C')

ax.set_title('Occupancy rate comparison of three hotels in the US from January to August 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Occupancy Rate')
ax.set_xticks(labels)
plt.legend(loc='best')
plt.grid()

plt.tight_layout()
plt.savefig('line chart/png/177.png')
plt.clf()