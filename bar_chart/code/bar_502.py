
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

x_data = np.arange(4)
plt.xticks(x_data,("North","South","East","West"))

plt.bar(x_data-0.2, [1200, 1400, 1600, 1400], label="Utility A", width=0.2, color='b')
plt.bar(x_data, [1400, 1600, 1800, 2000], label="Utility B", width=0.2, color='g')
plt.bar(x_data+0.2, [1000, 1200, 1400, 1600], label="Utility C", width=0.2, color='y')

plt.title("Energy consumption in three utilities across four regions in 2021")
plt.xlabel("Regions")
plt.ylabel("KWh")
plt.legend(loc="upper right")
plt.grid(True)
plt.tight_layout()
plt.savefig("bar chart/png/556.png")

plt.clf()