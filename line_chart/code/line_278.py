
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2019, 2020, 2021, 2022, 2023])
y1 = np.array([2500, 1800, 2200, 2100, 2300])
y2 = np.array([500, 400, 600, 550, 700])
y3 = np.array([900, 1000, 800, 750, 650])

fig = plt.figure(figsize=(8,6))
plt.plot(x, y1, label='Cinema ticket sales(million tickets)')
plt.plot(x, y2, label='Museum visitors(million people)')
plt.plot(x, y3, label='Theatre ticket sales(million tickets)')

plt.title('Arts and Culture Attendance and Ticket Sales in the US from 2019 to 2023')
plt.xlabel('Year')
plt.ylabel('Number')

plt.xticks(x)
plt.legend(loc='best')
plt.grid(linestyle='--')

plt.tight_layout()
plt.savefig('line chart/png/129.png')
plt.clf()