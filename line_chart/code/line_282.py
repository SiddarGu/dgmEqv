
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

x = [2011, 2012, 2013, 2014, 2015, 2016]
y1 = [100, 150, 180, 200, 220, 260]
y2 = [200, 220, 260, 280, 320, 350]

ax.plot(x, y1, color='red', label='Smartphone Sales')
ax.plot(x, y2, color='blue', label='Computer Sales')

ax.set(title="Growth of Smartphone and Computer Sales from 2011 to 2016",
       xlabel="Year",
       ylabel="Sales")

ax.legend(loc='best')
ax.grid()
plt.xticks(x)
plt.tight_layout()
plt.savefig('line chart/png/39.png')
plt.show()
plt.clf()