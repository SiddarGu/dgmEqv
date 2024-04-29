
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

year = [2020, 2021, 2022, 2023]
solar_power = [1000, 1200, 800, 1500]
wind_power = [800, 900, 1100, 1200]
hydro_power = [1200, 1100, 1300, 1400]

plt.plot(year, solar_power, label="Solar Power(GWh)", marker="o")
plt.plot(year, wind_power, label="Wind Power(GWh)", marker="o")
plt.plot(year, hydro_power, label="Hydro Power(GWh)", marker="o")

plt.xticks(year)
plt.title('Renewable Energy Sources in the US from 2020 to 2023')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3)

for a,b,c,d in zip(year,solar_power,wind_power,hydro_power):
    plt.annotate(str(b),xy=(a,b), ha='center', va='bottom', rotation=45, wrap=True)
    plt.annotate(str(c),xy=(a,c), ha='center', va='bottom', rotation=45, wrap=True)
    plt.annotate(str(d),xy=(a,d), ha='center', va='bottom', rotation=45, wrap=True)

plt.tight_layout()
plt.savefig('line chart/png/426.png')
plt.clf()