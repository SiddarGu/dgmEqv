
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))

Destination = ['USA','UK','Germany','France']
Hotels = [30,20,40,35]
Tourists = [45,40,47,44]

ax = plt.subplot()
ax.bar(Destination, Hotels, width=0.2, bottom=0, label='Hotels')
ax.bar(Destination, Tourists, width=0.2, bottom=Hotels, label='Tourists(hundred)')
ax.set_title('Number of hotels and tourists in four countries in 2021')
ax.set_ylabel('Number of hotels/tourists')
ax.set_xlabel('Destination')
ax.legend(loc='upper center')
plt.xticks(Destination, rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('bar_393.png')
plt.clf()