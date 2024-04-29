
import matplotlib.pyplot as plt
import numpy as np

data = [[2020, 65, 2.4, 6.2],
        [2021, 63, 2.2, 7.3],
        [2022, 62, 2.5, 8.4],
        [2023, 61, 2.7, 7.5],
        [2024, 60, 2.6, 6.3]]

years, temp, precip, speed = np.array(data).T

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.plot(years, temp, color='red', marker='o', label='Temperature (degrees Fahrenheit)')
ax.plot(years, precip, color='blue', marker='s', label='Precipitation (inches)')
ax.plot(years, speed, color='green', marker='^', label='Wind Speed (mph)')
ax.set_xticks(years)
ax.set_title('Average weather conditions in California from 2020 to 2024')
ax.legend(loc='upper center')

for i, txt in enumerate(temp):
    ax.annotate(txt, (years[i], temp[i]))
for i, txt in enumerate(precip):
    ax.annotate(txt, (years[i], precip[i]))
for i, txt in enumerate(speed):
    ax.annotate(txt, (years[i], speed[i]))

fig.tight_layout()
plt.savefig('line chart/png/210.png')
plt.clf()