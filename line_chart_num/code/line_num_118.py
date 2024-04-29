
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
renewable = [600, 650, 700, 800, 850, 900, 950, 1000]
fossil = [800, 900, 1000, 1100, 1200, 1400, 1500, 1600]

plt.plot(months, renewable, label="Renewable Energy Consumption (kWh)", linestyle="dashed")
plt.plot(months, fossil, label="Fossil Energy Consumption (kWh)")

plt.title("Comparison of Renewable and Fossil Energy Consumption in 2021")
plt.xlabel("Month")
plt.ylabel("Energy Consumption (kWh)")

plt.legend()
plt.grid()

for x,y in zip(months, renewable):
    plt.annotate(str(y), xy=(x,y), xytext=(-20,10), textcoords="offset points")

for x,y in zip(months, fossil):
    plt.annotate(str(y), xy=(x,y), xytext=(-20,10), textcoords="offset points")

plt.xticks(months)

plt.tight_layout()
plt.savefig('line chart/png/106.png')

plt.clf()