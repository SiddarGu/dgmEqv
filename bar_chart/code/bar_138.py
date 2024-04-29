

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
ax = plt.subplot()
ax.bar(["Europe", "Asia", "Africa", "America"], [2700, 3000, 2300, 2500], label="Restaurants", bottom=0, color="orange")
ax.bar(["Europe", "Asia", "Africa", "America"], [3500, 3700, 3200, 3500], label="Takeaways", bottom=2700, color="green")
ax.set_title("Number of Restaurants and Takeaways in four regions in 2021")
plt.xticks(rotation=45, ha="right", wrap=True)
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig("bar chart/png/423.png")
plt.clf()