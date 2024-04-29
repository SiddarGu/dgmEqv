
import matplotlib.pyplot as plt

x = ['January', 'February', 'March', 'April', 'May', 'June']
visitors = [20, 21, 22, 23, 24, 25]
likes = [10, 11, 12, 13, 14, 15]
shares = [15, 16, 17, 18, 19, 20]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(x, visitors, color='green', label='Visitors')
ax.plot(x, likes, color='red', label='Likes')
ax.plot(x, shares, color='blue', label='Shares')

plt.xticks(x)

ax.set_title('Increase in Social Media Engagement in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Engagements (million)')

ax.legend(loc='upper center')
ax.grid()

for x, y in zip(x, visitors):
    label = "{:.2f}".format(y)
    plt.annotate(label, 
                 (x,y), 
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')

for x, y in zip(x, likes):
    label = "{:.2f}".format(y)
    plt.annotate(label, 
                 (x,y), 
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')

for x, y in zip(x, shares):
    label = "{:.2f}".format(y)
    plt.annotate(label, 
                 (x,y), 
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')

plt.tight_layout()
plt.savefig('line chart/png/9.png')
plt.clf()