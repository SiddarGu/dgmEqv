
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2015, 1000, 1200, 800, 100], 
                 [2016, 1400, 1500, 900, 200], 
                 [2017, 1800, 1700, 1200, 400], 
                 [2018, 2000, 2000, 1500, 800],
                 [2019, 2500, 2500, 1800, 1000]])

fig = plt.figure(figsize=(8, 6))
ax = plt.subplot()

ax.plot(data[:, 0], data[:, 1], label='Instagram Users')
ax.plot(data[:, 0], data[:, 2], label='Facebook Users')
ax.plot(data[:, 0], data[:, 3], label='Twitter Users')
ax.plot(data[:, 0], data[:, 4], label='Snapchat Users')

ax.set_title('Growth of Social Media Users from 2015 to 2019')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Users')
ax.set_xticks(data[:, 0])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()

plt.savefig('line chart/png/52.png')
plt.clf()