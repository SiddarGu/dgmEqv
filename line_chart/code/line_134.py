

import matplotlib.pyplot as plt
import numpy as np

data = [[600,400,350],
        [650,450,380],
        [700,500,400],
        [750,550,420],
        [800,600,450],
        [850,650,480],
        [900,700,500],
        [800,650,450],
        [700,550,400],
        [650,500,380],
        [600,450,350],
        [550,400,320]]

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot()

ax.plot(months, [i[0] for i in data], label='Train Passengers', marker='o')
ax.plot(months, [i[1] for i in data], label='Bus Passengers', marker='*')
ax.plot(months, [i[2] for i in data], label='Airplane Passengers', marker='x')

ax.set_title('Public Transportation Passenger Usage in the United States in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Passengers (thousands)')

ax.legend(loc="upper left")
ax.grid(axis='y', linestyle='--')
ax.set_xticks(months)

plt.tight_layout()
plt.savefig('line chart/png/426.png')
plt.clf()