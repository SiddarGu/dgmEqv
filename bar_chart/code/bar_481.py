
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
ax = plt.subplot()
ax.bar(["2019","2020","2021","2022"],[100,105,110,120],width=0.6,bottom=0,label="Revenue")
ax.bar(["2019","2020","2021","2022"],[2,4,6,8],width=0.4,bottom=100,label="Growth rate")
ax.set_xticks(["2019","2020","2021","2022"])
plt.title("Revenue and growth rate of a business from 2019 to 2022")
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("bar chart/png/132.png")
plt.clf()