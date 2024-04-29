
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6)) 
ax = plt.subplot()
ax.bar(["USA","UK","Germany","France"],[20,30,10,25],label="Renewable Energy(%)",width=0.35)
ax.bar(["USA","UK","Germany","France"],[3000,3300,2000,2800],label="Carbon Emissions(tons)",bottom=[20,30,10,25],width=0.35)
ax.set_title("Percentage of renewable energy use and carbon emissions in four countries in 2021")
ax.set_ylabel("Percentage/tons")
ax.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.xticks(["USA","UK","Germany","France"])
plt.tight_layout()
plt.savefig("bar chart/png/540.png")
plt.clf()