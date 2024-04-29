
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plt.subplot()

year = [2000, 2001, 2002, 2003, 2004]
co2_emissions = [1000, 1200, 1400, 1600, 1800]
carbon_capture = [500, 600, 700, 800, 900]
renewable_energy = [200, 250, 300, 350, 400]

plt.plot(year, co2_emissions, label="CO2 Emissions (millions of tonnes)")
plt.plot(year, carbon_capture, label="Carbon Capture (millions of tonnes)")
plt.plot(year, renewable_energy, label="Renewable Energy Production (millions of tonnes)")

plt.title("Global Carbon Emissions and Carbon Capture Trends From 2000-2004")
plt.xlabel("Year")
plt.ylabel("Millions of Tonnes")
plt.xticks(year)
plt.legend(loc="best")

for a,b,c,d in zip(year, co2_emissions, carbon_capture, renewable_energy): 
    plt.annotate(str(b)+"/"+str(c)+"/"+str(d), xy=(a, b))

plt.grid()
plt.tight_layout()
plt.savefig("line chart/png/249.png")
plt.clf()