
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [2010, 50, 15, 0, 500], 
    [2011, 100, 30, 5, 1000], 
    [2012, 200, 50, 20, 3000],
    [2013, 400, 80, 50, 5000],
    [2014, 700, 150, 100, 7000],
    [2015, 1200, 250, 200, 9000]
])

x, fb, tw, ig, yt = data.T

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, fb, label='Facebook')
ax.plot(x, tw, label='Twitter')
ax.plot(x, ig, label='Instagram')
ax.plot(x, yt, label='Youtube')

ax.set_title('Growth of Social Media Platforms Users Over the Years')
ax.set_xlabel('Year')
ax.set_ylabel('Users (million)')
ax.set_xticks(x)
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig('line chart/png/181.png')
plt.clf()