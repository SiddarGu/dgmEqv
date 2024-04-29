
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
ax = plt.subplot()
ax.plot(["January", "February", "March", "April"], [10, 12, 14, 16], color="blue", linestyle="-", marker="o", label="Product A")
ax.plot(["January", "February", "March", "April"], [8, 9, 10, 12], color="red", linestyle="-", marker="o", label="Product B")
ax.plot(["January", "February", "March", "April"], [5, 7, 8, 10], color="green", linestyle="-", marker="o", label="Product C")
ax.set_xticks(["January", "February", "March", "April"])
ax.set_title("Price of three food products during Spring 2021")
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig("line chart/png/115.png")
plt.clf()