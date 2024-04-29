
import matplotlib.pyplot as plt
import numpy as np

month= ["January", "February", "March", "April", "May", "June", "July", "August"]
road_freight = [10, 15, 20, 25, 30, 35, 40, 45]
air_freight = [20, 25, 30, 35, 40, 45, 50, 55]
rail_freight = [30, 35, 40, 45, 50, 55, 60, 65]

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(1, 1, 1)
ax.plot(month, road_freight, label="Road Freight (tons)", marker="o", color="green")
ax.plot(month, air_freight, label="Air Freight (tons)", marker="^", color="blue")
ax.plot(month, rail_freight, label="Rail Freight (tons)", marker="s", color="red")

plt.xticks(np.arange(len(month)), month)

for a,b,c in zip(month, road_freight, air_freight): 
    ax.annotate(str(b), xy=(a, b), xytext=(-5, 5), textcoords='offset points')
    ax.annotate(str(c), xy=(a, c), xytext=(-5, 5), textcoords='offset points')

ax.legend(loc="best")
plt.title('Freight transport across different modes of transportation in 2020')
plt.tight_layout()
plt.savefig('line chart/png/349.png', bbox_inches='tight')
plt.clf()