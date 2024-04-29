
import matplotlib.pyplot as plt
plt.figure(figsize=(7,5))
ax = plt.subplot()
ax.bar(["USA","UK","Germany","France"],[180,200,230,210],label="Solar Energy(GWh)",width=0.2,bottom=0,align="edge")
ax.bar(["USA","UK","Germany","France"],[220,230,250,240],label="Wind Energy(GWh)",width=0.2,bottom=180,align="edge")
ax.bar(["USA","UK","Germany","France"],[480,440,420,460],label="Gas Energy(GWh)",width=0.2,bottom=400,align="edge")
ax.set_xticks(["USA","UK","Germany","France"])
ax.set_title("Energy production from solar, wind, and gas in four countries in 2021")
ax.legend()
plt.tight_layout()
plt.savefig("bar chart/png/359.png")
plt.close()