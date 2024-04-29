
import matplotlib.pyplot as plt

x = ['USA', 'UK', 'Germany', 'France']
y1 = [400, 450, 200, 350]
y2 = [50, 60, 40, 45]

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot()
ax.bar(x, y1, label='Connected Devices(million)', bottom=0, color='skyblue')
ax.bar(x, y2, label='Average Speed(Mbps)', bottom=y1, color='orange')

ax.set_title('Average internet speed and number of connected devices in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Values')

ax.annotate(y1[0], xy=(-0.2, y1[0]/2))
ax.annotate(y2[0], xy=(-0.2, y1[0]+y2[0]/2))
ax.annotate(y1[1], xy=(0.8, y1[1]/2))
ax.annotate(y2[1], xy=(0.8, y1[1]+y2[1]/2))
ax.annotate(y1[2], xy=(1.8, y1[2]/2))
ax.annotate(y2[2], xy=(1.8, y1[2]+y2[2]/2))
ax.annotate(y1[3], xy=(2.8, y1[3]/2))
ax.annotate(y2[3], xy=(2.8, y1[3]+y2[3]/2))

ax.legend()
plt.xticks(x)
plt.tight_layout()
plt.savefig('Bar Chart/png/292.png')
plt.clf()