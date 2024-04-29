
import matplotlib.pyplot as plt 
import numpy as np

data = [['Jan', 120, 150], 
        ['Feb', 130, 140], 
        ['Mar', 140, 130], 
        ['Apr', 150, 140], 
        ['May', 160, 150], 
        ['Jun', 170, 160], 
        ['Jul', 180, 170], 
        ['Aug', 190, 180], 
        ['Sep', 200, 190], 
        ['Oct', 210, 200], 
        ['Nov', 220, 210], 
        ['Dec', 230, 220]]

months, online, in_store = np.array(data).T

fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)

ax.plot(months, online, label = 'Online', color = 'b', marker = 'o')
ax.plot(months, in_store, label = 'In-store', color = 'r', marker = 'o')

ax.set_title('Comparison of online and in-store purchases in 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Purchases (millions)')

ax.legend(loc='upper right')
ax.grid(axis='y', linestyle='-')

for i, txt in enumerate(online):
    ax.annotate(txt, (months[i],online[i]))
for i, txt in enumerate(in_store):
    ax.annotate(txt, (months[i],in_store[i]))

ax.set_xticks(months)
ax.tick_params(axis='x', rotation=45)

fig.tight_layout()

plt.savefig('line chart/png/597.png')
plt.clf()