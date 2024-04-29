
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot()
country = ["USA", "UK", "Germany", "France"]
Agriculture = [50, 45, 35, 40]
Manufacturing = [25, 30, 40, 35]
Services = [25, 25, 25, 25]
bottom = [0, 0, 0, 0]
ax.bar(country, Agriculture, label="Agriculture", bottom=bottom, width=0.3, color="g")
ax.bar(country, Manufacturing, label="Manufacturing", bottom=Agriculture, width=0.3, color="b")
ax.bar(country, Services, label="Services", bottom=[Agriculture[i] + Manufacturing[i] for i in range(len(country))], width=0.3, color="y")
plt.xticks(country)
plt.legend(loc="upper right")
plt.title("Percentage of Agriculture, Manufacturing, and Services industries in four countries in 2021")
plt.tight_layout()
plt.savefig("bar chart/png/408.png")
plt.clf()