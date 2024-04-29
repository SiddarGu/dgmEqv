
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

year = [2017, 2018, 2019, 2020, 2021]
users = [1, 2, 3, 4, 5]
time_spent = [50, 75, 100, 125, 150]

ax.plot(year, users,label='Users(million)', color='green')
ax.plot(year, time_spent, label='Time spent(hours)', color='red')

ax.set_title('Increase in Social Media Usage and Time Spent Over Five Years')
ax.set_xlabel('Year')
ax.set_xticks(year)

ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.02, 1., 0.102), ncol=2, mode="expand", borderaxespad=0., fontsize='large')
plt.tight_layout()
plt.savefig('line chart/png/557.png')
plt.clf()