
import matplotlib.pyplot as plt
import numpy as np

data = {'USA': [25, 75, 600], 
        'UK': [30, 70, 470], 
        'Germany': [40, 60, 400], 
        'France': [35, 65, 430]}

country = list(data.keys())
Renewable_Energy_Usage = np.array([data[i][0] for i in country])
Fossil_Fuel_Usage = np.array([data[i][1] for i in country])
Carbon_Emissions = np.array([data[i][2] for i in country])

x = np.arange(len(country))
width = 0.3

fig, ax = plt.subplots(figsize=(8,6))
ax.bar(x-width, Renewable_Energy_Usage, width=width, label="Renewable Energy Usage (%)", color='green')
ax.bar(x, Fossil_Fuel_Usage, width=width, label="Fossil Fuel Usage (%)", color='brown')
ax.bar(x+width, Carbon_Emissions, width=width, label="Carbon Emissions (million tons)", color='red')

plt.xticks(x, country)
plt.xlabel("Country")
plt.title("Comparison of renewable energy usage, fossil fuel usage and carbon emissions in four countries in 2021")
plt.legend(loc="upper left")

# Annotate the values
for i in range(len(country)):
    ax.annotate(Renewable_Energy_Usage[i], xy=(x[i]-width, Renewable_Energy_Usage[i]+2), fontsize=10)
    ax.annotate(Fossil_Fuel_Usage[i], xy=(x[i], Fossil_Fuel_Usage[i]+2), fontsize=10)
    ax.annotate(Carbon_Emissions[i], xy=(x[i]+width, Carbon_Emissions[i]+2), fontsize=10)

plt.tight_layout()
plt.savefig("Bar Chart/png/526.png")
plt.clf()