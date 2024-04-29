
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

Type = ['Concerts', 'Exhibitions', 'Theater'] 
Price = [50, 20, 30]
Attendance = [500, 350, 400]

ax.bar(Type, Price, label='Price')
ax.bar(Type, Attendance, bottom=Price,label='Attendance')

ax.set_title('Prices and Attendance at Cultural Events in 2021')
ax.set_xlabel('Type')
ax.set_ylabel('Number')
ax.legend()

for x, y in zip(Type, Price):
    ax.annotate(y, xy=(x, y+10), ha='center', va='bottom')
for x, y1, y2 in zip(Type, Price, Attendance):
    ax.annotate(y2, xy=(x, y1+y2/2), ha='center', va='bottom')

plt.xticks(Type)
plt.tight_layout()
plt.savefig('Bar Chart/png/357.png')
plt.clf()