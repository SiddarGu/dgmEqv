
import matplotlib.pyplot as plt
import numpy as np

data = [[100, 200, 500], [150, 250, 700], [175, 300, 800], [225, 350, 900], [250, 400, 1000], [300, 450, 1100], [325, 500, 1300]]

x = np.arange(len(data))

plt.figure(figsize=(10, 6))
ax = plt.subplot()
ax.set_xticks(x)
ax.set_xticklabels(["January", "February", "March", "April", "May", "June", "July"])

plt.plot(x, [i[0] for i in data], color='red', label="Number of Users(million)")
plt.plot(x, [i[1] for i in data], color='green', label="Number of Likes(million)")
plt.plot(x, [i[2] for i in data], color='blue', label="Number of Tweets(million)")

plt.title("Social Media Trends in 2021")
plt.xlabel("Month")
plt.ylabel("Number of Users/Likes/Tweets(million)")
plt.legend(loc="upper left")
plt.tight_layout()
fig = plt.gcf()
fig.savefig('line chart/png/200.png')
plt.clf()