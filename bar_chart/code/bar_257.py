
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
Mode_of_transport = ["Road", "Rail", "Air", "Sea"]
Distance = [1000, 800, 600, 400]
Cost = [500, 400, 450, 300]
ax.bar(Mode_of_transport, Distance, bottom=Cost, label="Distance")
ax.bar(Mode_of_transport, Cost, label="Cost")
plt.title("Cost of transportation via different modes of transport over a certain distance in 2021")
ax.legend()
plt.xticks(Mode_of_transport)
plt.tight_layout()
plt.savefig('bar chart/png/523.png')
plt.clf()