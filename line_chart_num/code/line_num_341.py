
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.subplot(111)

x = [2015, 2016, 2017, 2018, 2019]
y1 = [320, 400, 500, 630, 780]
y2 = [1120, 1300, 1450, 1600, 1850]
y3 = [400, 500, 600, 700, 800]
y4 = [200, 220, 240, 260, 290]

plt.plot(x, y1, marker='o', label='Twitter users (million)')
plt.plot(x, y2, marker='s', label='Facebook users (million)')
plt.plot(x, y3, marker='^', label='Instagram users (million)')
plt.plot(x, y4, marker='*', label='Snapchat users (million)')

for i, j in zip(x, y1):
    plt.annotate(str(j), xy=(i, j))
for i, j in zip(x, y2):
    plt.annotate(str(j), xy=(i, j))
for i, j in zip(x, y3):
    plt.annotate(str(j), xy=(i, j))
for i, j in zip(x, y4):
    plt.annotate(str(j), xy=(i, j))

plt.title('Number of users in popular social media networks from 2015 to 2019')
plt.xticks(x, rotation=30)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/40.png')
plt.clf()