
import matplotlib.pyplot as plt
import numpy as np

x_data = [2015, 2016, 2017, 2018, 2019]
y1_data = [80, 90, 100, 120, 140]
y2_data = [10, 12, 14, 18, 20]

plt.figure(figsize=(8, 6))
ax = plt.subplot()
ax.set_xticks(x_data)
ax.plot(x_data, y1_data, label="Number of Students", c='r', marker='o')
ax.plot(x_data, y2_data, label="Number of Teachers", c='b', marker='o')

plt.title('Increase in student-teacher ratio in a school from 2015 to 2019')
plt.xlabel('Year')
plt.ylabel('Number')
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig('line chart/png/184.png')
plt.clf()