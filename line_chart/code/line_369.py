
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

month = ['January', 'February', 'March', 'April', 'May']
railway = [3000, 3200, 3500, 4000, 3800]
airline = [4000, 4400, 4100, 4500, 4300]
highway = [5000, 5500, 6000, 6500, 7000]

plt.xlabel('Month', fontsize=15)
plt.ylabel('Number of Passengers', fontsize=15)
plt.title('Transportation comparison in terms of passengers in the USA from January to May, 2021', fontsize=15)

plt.plot(month, railway, label='Railway', linewidth=3)
plt.plot(month, airline, label='Airline', linewidth=3)
plt.plot(month, highway, label='Highway', linewidth=3)

plt.xticks(month, rotation=45)
plt.legend(fontsize=15, bbox_to_anchor=(1, 0.3))

plt.tight_layout()
plt.savefig('line chart/png/90.png')
plt.clf()