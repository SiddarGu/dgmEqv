
import matplotlib.pyplot as plt
x = ['January', 'February', 'March', 'April', 'May', 'June']
y1 = [1.25, 1.50, 1.75, 2.00, 2.25, 2.50]
y2 = [2.50, 2.75, 3.00, 3.25, 3.50, 3.75]
y3 = [3.75, 4.00, 4.25, 4.50, 4.75, 5.00]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.plot(x, y1, label='Average Price of Produce A(USD)')
ax.plot(x, y2, label='Average Price of Produce B(USD)')
ax.plot(x, y3, label='Average Price of Produce C(USD)')
ax.set_title('Average Monthly Prices of Produce in the Food and Beverage Industry')
ax.set_xticks(x)
ax.legend(loc='best', fontsize='small', ncol=3, bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig('line chart/png/483.png')
plt.clf()