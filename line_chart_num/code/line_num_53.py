
import matplotlib.pyplot as plt
import numpy as np

data = [['January', 20, 50], 
        ['February', 25, 45], 
        ['March', 30, 40], 
        ['April', 35, 45], 
        ['May', 40, 50], 
        ['June', 45, 55], 
        ['July', 50, 60], 
        ['August', 60, 65]]

months, online_sales, retail_sales = np.array(data).T

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

ax.plot(months, online_sales, color='r', linewidth=2, label='Online Sales')
ax.plot(months, retail_sales, color='b', linewidth=2, label='Retail Sales')

ax.set_title('Comparison of Online and Retail Sales in 2020')
ax.set_xlabel('Months')
ax.set_ylabel('Sales(million dollars)')

ax.legend(loc='upper left')
ax.grid(True)

ax.set_xticks(months)

for x, y1, y2 in zip(months, online_sales, retail_sales):
    ax.annotate('(%s, %s)' % (y1, y2), xy=(x, y1))
    ax.annotate('(%s, %s)' % (y1, y2), xy=(x, y2))

plt.tight_layout()
plt.savefig('line chart/png/307.png')
plt.clf()