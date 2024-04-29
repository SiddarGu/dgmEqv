
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6))
ax = plt.subplot(1,1,1)
Year = [2018, 2019, 2020, 2021]
Attendance = [5000, 10000, 15000, 20000]
Viewership = [500000, 800000, 1000000, 1200000]
ax.plot(Year, Attendance, label='Attendance', color='b', linestyle='-', marker='o')
ax.plot(Year, Viewership, label='Viewership', color='r', linestyle='-', marker='^')
plt.xticks(np.arange(min(Year), max(Year)+1, 1))
plt.title('Attendance and Viewership for a Sports Event from 2018-2021')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/536.png')
plt.clf()