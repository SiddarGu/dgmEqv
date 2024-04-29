
import matplotlib.pyplot as plt
import numpy as np

data = [[50, 50], [55, 45], [45, 55], [35, 65], [20, 80], [10, 90]]
x = np.arange(6)
male = [i[0] for i in data]
female = [i[1] for i in data]

plt.figure(figsize=(10, 6))
ax = plt.subplot()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position('zero')
plt.xticks(x, ('0-14', '15-29', '30-44', '45-59', '60-74', '75+'))
plt.plot(x, male, label='Male(%)', linestyle='-.', marker='o', color='b')
plt.plot(x, female, label='Female(%)', linestyle='--', marker='o', color='r')
plt.title('Gender distribution among different age groups in the US')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/508.png')
plt.cla()