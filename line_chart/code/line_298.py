
import matplotlib.pyplot as plt
import numpy as np

data = [['January',25,50],['February',27,55],['March',30,58],['April',29,51],['May',31,60],['June',32,62],['July',34,65],['August',36,68]]

x_axis = [row[0] for row in data]
online_sales = [row[1] for row in data]
retail_sales = [row[2] for row in data]

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot()
ax.plot(x_axis, online_sales, linestyle='-', marker='o', color='b', label='Online Sales')
ax.plot(x_axis, retail_sales, linestyle='-', marker='o', color='r', label='Retail Sales')
ax.set_title('Comparison of Online and Retail Sales from January to August 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Sales (billion dollars)')
ax.legend()
plt.xticks(x_axis, rotation=90)
plt.tight_layout()
plt.savefig('line chart/png/449.png')
plt.clf()