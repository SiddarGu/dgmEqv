
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
ax = plt.subplot()
x = ['January', 'February', 'March', 'April', 'May']
y1 = [5000, 6000, 7000, 8000, 9000]
y2 = [6000, 7000, 8000, 9000, 7000]
y3 = [8000, 9000, 9000, 7000, 6000]
y4 = [9000, 8000, 7000, 6000, 5000]
ax.plot(x, y1, label='Production A(units)', color='b', marker='o', linestyle='--')
ax.plot(x, y2, label='Production B(units)', color='r', marker='s', linestyle='--')
ax.plot(x, y3, label='Production C(units)', color='g', marker='^', linestyle='--')
ax.plot(x, y4, label='Production D(units)', color='k', marker='d', linestyle='--')
ax.set_title('Production of four types of goods in the first half of 2021') 
ax.set_xlabel('Month')
ax.set_ylabel('Units')
ax.set_xticks(x)
ax.legend(loc='upper left')
plt.tight_layout() 
plt.savefig('line chart/png/559.png')
plt.clf()