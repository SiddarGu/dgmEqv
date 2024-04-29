
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
ax = plt.subplot()

months = ["January","February","March","April","May","June"]
air = [250, 300, 350, 400, 450, 500]
sea = [500, 600, 700, 800, 900, 1000]
truck = [1000, 1100, 1300, 1500, 1600, 1800]
plt.plot(months, air, color="skyblue", linewidth=2, label="Air Freight(tons)")
plt.plot(months, sea, color="red", linewidth=2, label="Sea Freight(tons)")
plt.plot(months, truck, color="green", linewidth=2, label="Truck Freight(tons)")

plt.title("Freight Transportation Volume in the US in 2020")
plt.xlabel("Month")
plt.ylabel("Volume")

plt.xticks(months, rotation = 45)

for a,b,c in zip(months,air,sea):
    plt.annotate('Air:'+str(b)+'\n'+'Sea:'+str(c), xy=(a,b), xytext=(0,5), textcoords='offset points',rotation=-30,ha="center")

plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("line chart/png/316.png")
plt.clf()