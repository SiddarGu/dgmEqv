
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

states = ["California", "Texas", "New York", "Florida"]
home_price = [500000, 400000, 600000, 450000]
rental_price = [2500, 2000, 3000, 2200]

ax.bar(states, home_price, label="Home Price", color="b", bottom=0)
ax.bar(states, rental_price, label="Rental Price", color="r", bottom=home_price)

plt.legend(loc="upper left")
plt.title("Average home and rental prices in four states in 2021")
plt.xlabel("State")
plt.ylabel("Price")
plt.xticks(states, rotation=45, ha="right")
plt.tight_layout()
plt.savefig("bar chart/png/417.png")
plt.clf()