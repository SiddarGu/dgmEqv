
import matplotlib.pyplot as plt
import pandas as pd

x = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00'] 
y1 = [20,22,19,17,18,21,23,20]
y2 = [25,27,24,26,29,30,28,25]
y3 = [30,35,32,40,36,38,31,30]

data = {'time':x, 'Number of Visitors(million)':y1, 'Number of Posts(million)':y2, 'Number of Likes(million)':y3}

df = pd.DataFrame(data)

plt.figure(figsize=(10,6))
ax = plt.subplot(1,1,1)
ax.plot(x, y1, label='Number of Visitors(million)', marker='o', color='b')
ax.plot(x, y2, label='Number of Posts(million)', marker='o', color='r')
ax.plot(x, y3, label='Number of Likes(million)', marker='o', color='g')

plt.title('Social Media Activity during peak hours on March 19, 2023')
ax.set_xticks(x)
ax.set_xticklabels(x, rotation=45, ha='right')
ax.set_ylabel('Number of Visitors/Posts/Likes')
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('line chart/png/240.png')
plt.clf()