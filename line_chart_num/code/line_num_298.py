
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
online_sales = [500, 550, 600, 650, 700, 750]
retail_sales = [800, 850, 900, 950, 1000, 1050]
total_sales = [1300, 1400, 1500, 1600, 1700, 1800]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(months, online_sales, label="Online Sales (billion dollars)")
ax.plot(months, retail_sales, label="Retail Sales (billion dollars)")
ax.plot(months, total_sales, label="Total Sales (billion dollars)")

ax.set_title("Comparison of Online and Retail Sales from January to June 2021")

ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months)

ax.legend(loc='best')

for i, j in enumerate(online_sales):
    ax.annotate(str(j), xy=(i, j+10))
for i, j in enumerate(retail_sales):
    ax.annotate(str(j), xy=(i, j+10))
for i, j in enumerate(total_sales):
    ax.annotate(str(j), xy=(i, j+10))

fig.tight_layout()
plt.savefig('line chart/png/186.png')
plt.clf()