
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1000000, 2000000],
                 [1100000, 2300000],
                 [1150000, 2500000],
                 [1200000, 2700000],
                 [1250000, 3000000],
                 [1300000, 3200000]])

x = np.arange(6) 
labels = ['2021-02-01', '2021-02-15', '2021-03-01', '2021-03-15', '2021-04-01', '2021-04-15']

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, data[:,0], 'b-', label='Number of Users')
ax.plot(x, data[:,1], 'g-', label='Number of Devices')

ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, wrap=True)

ax.set_title('Growth of users and devices connected to the Internet in 2021')
ax.legend()

plt.tight_layout()
plt.savefig('line chart/png/372.png')
plt.clf()