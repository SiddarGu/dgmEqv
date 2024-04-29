
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12, 8)) 
ax = fig.add_subplot(111) 

country_data = [["USA",20,5], ["UK",15,7], ["Germany",13,6], ["France",12,4]]
data = list(zip(*country_data))

ax.bar(data[0], data[1], color='b', bottom=data[2], label='GDP')
ax.bar(data[0], data[2], color='r', label='Investment')

ax.set_title('Gross Domestic Product and Investment in four countries in 2021')
ax.set_ylabel('Billion')
ax.legend(loc='best')
ax.grid(True)

for i, v in enumerate(data[1]):
    ax.text(i, v + 0.5, str(v), color='blue', fontweight='bold')
for i, v in enumerate(data[2]):
    ax.text(i, v + 0.5, str(v), color='red', fontweight='bold')

ax.set_xticks(range(len(data[0])))
ax.set_xticklabels(data[0])
plt.tight_layout()
plt.savefig('Bar Chart/png/69.png')
plt.clf()