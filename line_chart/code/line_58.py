
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(16, 8))

x = np.arange(2011, 2016)
A_users = [400, 500, 700, 1000, 1300]
B_users = [300, 400, 500, 700, 900]
C_users = [500, 600, 800, 900, 1100]

plt.plot(x, A_users, label='Social Media A')
plt.plot(x, B_users, label='Social Media B')
plt.plot(x, C_users, label='Social Media C')

plt.title('Growth of Social Media Platforms Usage from 2011 to 2015', fontsize=14)

plt.xticks(np.arange(2011, 2016, step=1))
plt.xlabel('Years', fontsize=14)
plt.ylabel('Amount of Users (million)', fontsize=14)
plt.legend(loc='upper left', fontsize=14)
plt.grid(axis='y')

plt.tight_layout()
plt.savefig('line chart/png/145.png')
plt.clf()