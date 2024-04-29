
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot()
states=["California","New York","Florida","Texas"]
solar_energy=[18000,21000,22000,17000]
wind_energy=[20000,19000,18000,20000]
hydro_energy=[14000,16000,17000,15000]
x=range(len(states))
ax.bar(x, solar_energy, label="Solar Energy(kWh)", width=0.2, bottom=0)
ax.bar(x, wind_energy, label="Wind Energy(kWh)", width=0.2, bottom=solar_energy)
ax.bar(x, hydro_energy, label="Hydro Energy(kWh)", width=0.2, bottom=[sum(x) for x in zip(solar_energy, wind_energy)])
ax.set_xticks(x)
ax.set_xticklabels(states,rotation=45,ha="right")
ax.set_title("Renewable energy production in four states in 2021")
ax.legend(loc="best")
plt.tight_layout()
plt.savefig("bar chart/png/327.png")
plt.clf()