
import matplotlib.pyplot as plt
import numpy as np

months = np.array(["January","February","March","April","May"])
cropA = np.array([500,400,600,800,500])
cropB = np.array([400,500,400,700,800])
cropC = np.array([600,700,500,400,600])
cropD = np.array([800,900,1000,500,400])

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)
ax.plot(months,cropA,label="Crop A(tons)",c="blue")
ax.plot(months,cropB,label="Crop B(tons)",c="red")
ax.plot(months,cropC,label="Crop C(tons)",c="green")
ax.plot(months,cropD,label="Crop D(tons)",c="orange")

ax.grid(True,linestyle="-.",color="gray",alpha=0.5)
ax.set_title("Crop Production in a Farming Community in 2021")
ax.set_xlabel("Month")
ax.set_ylabel("Crop Production (tons)")
ax.legend(loc="upper left",bbox_to_anchor=(1,1))
plt.xticks(months,rotation=45,fontsize=7)
plt.tight_layout()
plt.savefig(r"line chart/png/432.png")
plt.clf()