
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))

country=['USA','UK','Germany','France']
donations_received=[1000,900,1200,1300]
donations_made=[800,1100,1400,1200]

plt.plot(country, donations_received, label="Donations Received", color="blue", marker="o", linestyle="-")
plt.plot(country, donations_made, label="Donations Made", color="red",marker="o", linestyle="-")

plt.xlabel("Country")
plt.ylabel("Donations (million dollars)")
plt.title("Donations Received and Made in Selected Countries in 2021")
plt.legend(loc="upper right", fontsize="small")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("line chart/png/359.png")
plt.clf()