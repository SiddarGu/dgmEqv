
import matplotlib.pyplot as plt
import numpy as np

Month = ['January', 'February', 'March', 'April', 'May']
Airplane_Tickets_Sold = [400, 500, 600, 700, 800]
Train_Tickets_Sold = [500, 600, 700, 800, 900]
Bus_Tickets_Sold = [800, 900, 1000, 1100, 1200]

plt.figure(figsize=(15, 8))

plt.plot(Month, Airplane_Tickets_Sold, label="Airplane Tickets Sold", color="b", linestyle="-", marker="o")
plt.plot(Month, Train_Tickets_Sold, label="Train Tickets Sold", color="r", linestyle="-", marker="o")
plt.plot(Month, Bus_Tickets_Sold, label="Bus Tickets Sold", color="g", linestyle="-", marker="o")

plt.title("Comparison of Transportation Tickets Sold in the First Half of 2021")
plt.xlabel("Month")
plt.ylabel("Tickets Sold")

plt.xticks(np.arange(len(Month)), Month)
plt.legend(loc="upper left")

for a, b, c in zip(Month, Airplane_Tickets_Sold, Train_Tickets_Sold):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10, color="b")
    plt.text(a, c, c, ha='center', va='bottom', fontsize=10, color="r")

for a, b, c in zip(Month, Train_Tickets_Sold, Bus_Tickets_Sold):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10, color="r")
    plt.text(a, c, c, ha='center', va='bottom', fontsize=10, color="g")

plt.tight_layout()
plt.savefig("line chart/png/463.png")
plt.clf()