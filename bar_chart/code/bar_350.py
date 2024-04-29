
import matplotlib.pyplot as plt

Country = ["USA", "UK", "Germany", "France"]
CO2_Emission = [7000, 6000, 5000, 4000]
Renewable_Energy = [30, 20, 40, 50]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()
ax.bar(Country, CO2_Emission, label="CO2 Emission (tonnes)", width=0.6)
ax.bar(Country, Renewable_Energy, bottom=CO2_Emission, label="Renewable Energy (%)", width=0.6)
ax.set_title("CO2 emission and renewable energy usage in four countries in 2021")
ax.legend()
ax.set_xticklabels(Country, rotation=45, ha="right", wrap=True)
plt.tight_layout()
plt.savefig("bar chart/png/306.png")
plt.clf()