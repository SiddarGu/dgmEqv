
import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
truck_loads = [1000, 900, 800, 1100, 1200, 1000, 1400, 1200, 1000, 900, 800, 700]
rail_loads = [200, 250, 300, 400, 350, 280, 250, 200, 150, 100, 50, 25]
air_loads = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

plt.figure(figsize=(12, 8))
plt.plot(months, truck_loads, label="Truck Loads", marker='o')
plt.plot(months, rail_loads, label="Rail Loads", marker='o')
plt.plot(months, air_loads, label="Air Loads", marker='o')

plt.title("Freight Delivery Loads by Mode of Transportation in 2021", fontsize=14)
plt.xlabel("Months", fontsize=14)
plt.ylabel("Loads", fontsize=14)
plt.xticks(months)

for i in range(len(months)):
    plt.annotate(truck_loads[i], xy=(i, truck_loads[i]), xytext=(5, 0), 
                 textcoords="offset points", ha='left', va='center')
    plt.annotate(rail_loads[i], xy=(i, rail_loads[i]), xytext=(5, 0), 
                 textcoords="offset points", ha='left', va='center')
    plt.annotate(air_loads[i], xy=(i, air_loads[i]), xytext=(5, 0), 
                 textcoords="offset points", ha='left', va='center')

legend_properties = {'weight':'bold'}
plt.legend(prop=legend_properties, loc='upper left')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('line chart/png/26.png')
plt.clf()