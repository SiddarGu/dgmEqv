
import matplotlib.pyplot as plt
plt.figure(figsize=(7,5),dpi=200)
plt.title("Donations to four charities over 4 years", fontsize=14)
plt.plot(["2019","2020","2021","2022"],[50,60,70,80],label="Donations A(million dollars)")
plt.plot(["2019","2020","2021","2022"],[60,50,80,80],label="Donations B(million dollars)")
plt.plot(["2019","2020","2021","2022"],[70,80,50,95],label="Donations C(million dollars)")
plt.plot(["2019","2020","2021","2022"],[90,80,95,100],label="Donations D(million dollars)")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Donations (million dollars)", fontsize=12)
plt.xticks(["2019","2020","2021","2022"])
plt.legend(loc="best")
for a,b in zip(["2019","2020","2021","2022"],[50,60,70,80]):
    plt.text(a, b, b, ha='center', va='bottom',fontsize=10)
for a,b in zip(["2019","2020","2021","2022"],[60,50,80,80]):
    plt.text(a, b, b, ha='center', va='bottom',fontsize=10)
for a,b in zip(["2019","2020","2021","2022"],[70,80,50,95]):
    plt.text(a, b, b, ha='center', va='bottom',fontsize=10)
for a,b in zip(["2019","2020","2021","2022"],[90,80,95,100]):
    plt.text(a, b, b, ha='center', va='bottom',fontsize=10)
plt.grid(linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("line chart/png/217.png")
plt.clf()