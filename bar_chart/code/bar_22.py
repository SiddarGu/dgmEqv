
import matplotlib.pyplot as plt

Region = ["South","MidWest","West","NorthEast"]
Median_Home_Price = [300000,250000,400000,350000]
Average_Rent = [1500,1300,2000,1700]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()
ax.bar(Region, Median_Home_Price, label="Median Home Price", width=0.4, color="red")
ax.bar(Region, Average_Rent, label="Average Rent", width=0.4, bottom=Median_Home_Price, color="blue")
plt.title("Median Home Prices and Average Rents across four regions in 2021")
ax.legend(loc="upper center")
plt.xticks(Region)
plt.tight_layout()
plt.savefig("bar chart/png/214.png")
plt.clf()