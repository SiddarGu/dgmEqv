
import matplotlib.pyplot as plt

region = ["Asia", "Europe", "North America", "South America"]
airplane_trips = [1000, 1200, 1400, 1600]
trucks_trips = [3000, 3400, 3600, 3800]
ships_trips = [1500, 1700, 1900, 2100]

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(region, airplane_trips, label="Airplane Trips", width=0.25, bottom=trucks_trips)
ax.bar(region, trucks_trips, label="Trucks Trips", width=0.25, bottom=ships_trips)
ax.bar(region, ships_trips, label="Ships Trips", width=0.25)

ax.set_title("Number of trips made by airplane, truck and ship in four regions in 2021")
ax.set_xticklabels(region, rotation=45, ha="right", wrap=True)
ax.legend(loc="upper right")

ax.set_xlabel("Region")
ax.set_ylabel("Trips")

plt.tight_layout()
plt.savefig("bar chart/png/353.png")
plt.clf()