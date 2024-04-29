
import matplotlib.pyplot as plt
plt.figure(figsize=(13, 8))
ax = plt.subplot()

year = [2020, 2021, 2022, 2023]
wind = [4000, 5000, 6000, 7000]
solar = [6000, 7000, 8000, 9000]
hydro = [8000, 9000, 10000, 11000]

ax.plot(year, wind, color='orange', label='Wind Energy Production (MWh)')
ax.plot(year, solar, color='green', label='Solar Energy Production (MWh)')
ax.plot(year, hydro, color='blue', label='Hydroelectric Production (MWh)')

ax.set_title('Renewable energy production in the United States from 2020 to 2023')
ax.set_xlabel('Year')
ax.set_ylabel('Energy Production (MWh)')
ax.set_xticks(year)
ax.set_xticklabels(year)
ax.legend(loc='upper left', bbox_to_anchor=(0, 1))

plt.tight_layout()
plt.savefig('line chart/png/248.png')
plt.clf()