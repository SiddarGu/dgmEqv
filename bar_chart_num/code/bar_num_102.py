
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 200, 50], 
        ['UK', 80, 35], 
        ['Germany', 100, 42], 
        ['France', 120, 48]]

fig = plt.figure()
ax = fig.add_subplot()

country = np.arange(len(data))
users = [x[1] for x in data]
speed = [x[2] for x in data]

ax.bar(country, users, color='b', label='Users')
ax.bar(country, speed, bottom=users, color='g', label='Internet Speed (Mbps)')
ax.set_xticks(country)
ax.set_xticklabels([x[0] for x in data])
ax.set_title('Number of Internet Users and Average Internet Speed in four countries in 2021')
ax.legend()

for i in range(len(data)):
    x = i 
    y = users[i] + speed[i] /2
    ax.annotate(str(users[i]) + ', ' + str(speed[i]), xy=(x, y))

fig.tight_layout()
plt.savefig('Bar Chart/png/117.png', dpi=100)
plt.clf()