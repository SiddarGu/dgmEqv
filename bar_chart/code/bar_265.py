
import matplotlib.pyplot as plt

country = ["USA","UK","Germany","France"]
manufacturing_cost = [500,550,600,650]
manufacturing_output = [750,800,850,900]

plt.figure(figsize=(10, 8))
ax = plt.subplot()
plt.bar(country, manufacturing_cost, label="Manufacturing Cost", bottom=0)
plt.bar(country, manufacturing_output, label="Manufacturing Output", bottom=manufacturing_cost)
plt.xticks(rotation=45)
ax.set_title("Manufacturing Cost and Output in four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Unit Number")
ax.legend(loc="upper center")
plt.tight_layout()
plt.savefig("bar chart/png/252.png")
plt.clf()