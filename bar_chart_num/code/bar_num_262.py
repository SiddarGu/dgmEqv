
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA", "UK", "Germany", "France"]
Renewable_Energy_Usage = np.array([20, 25, 30, 35])
Air_Quality_Index = np.array([80, 76, 90, 92])

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot()

ax.bar(Country, Renewable_Energy_Usage, label='Renewable Energy Usage %', bottom=0, color='#FF7F50')
ax.bar(Country, Air_Quality_Index, label='Air Quality Index', bottom=Renewable_Energy_Usage, color='#87CEFA')

ax.set_title('Renewable Energy Usage and Air Quality Index in Four Countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Value')
ax.legend()
ax.grid(True, axis='y', color='#DCDCDC')

for i in range(len(Country)):
    ax.annotate(str(Renewable_Energy_Usage[i]) + '\n' + str(Air_Quality_Index[i]), xy=(i, Renewable_Energy_Usage[i] + Air_Quality_Index[i]/2), ha='center', va='center')

plt.xticks(Country)
plt.tight_layout()
plt.savefig('Bar Chart/png/411.png')
plt.clf()