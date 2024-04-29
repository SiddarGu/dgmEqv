
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

x_data = ['Sales', 'Production', 'Administration', 'Support']
y_data1 = [4000, 5000, 3000, 2000]
y_data2 = [40, 45, 35, 30]

ax.bar(x_data, y_data1, color='#ff9999', label='Average Salary(USD)')
ax.bar(x_data, y_data2, bottom=y_data1, color='#99ccff', label='Average Hours')

plt.xticks(np.arange(len(x_data)), x_data, rotation=45, fontsize=10)
plt.title('Average salary and hours of four employee roles in 2021')
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('bar chart/png/496.png')
plt.clf()