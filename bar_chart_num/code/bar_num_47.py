
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111)

region = ['North America', 'Europe', 'Asia', 'Africa']
carbon = [1000, 1300, 2000, 500]
renew = [20, 30, 15, 10]

bar1 = ax.bar(region, carbon, width=0.4, label='Carbon Emission(million tons)', bottom=0)
bar2 = ax.bar(region, renew, width=0.4, label='Renewable Energy(%)', bottom=carbon)

plt.xticks(region, rotation='vertical')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
plt.title('Carbon emission and renewable energy in four regions in 2021')
for i, v in enumerate(carbon):
    ax.text(i-0.2, v+renew[i]/2, str(v), color='blue', fontweight='bold')
for i, v in enumerate(renew):
    ax.text(i+0.2, v/2, str(v), color='green', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/372.png')
plt.clf()