
import matplotlib.pyplot as plt

values = [30,50,100000,45,75,120000,40,65,110000,35,60,105000]
regions = ["East Coast","West Coast","Central","South"]

plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.bar(regions, values[:4], label = "Hotels")
ax.bar(regions, values[4:8], bottom = values[:4], label = "Restaurants")
ax.bar(regions, values[8:], bottom = values[4:8], label = "Travelers")
ax.legend()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
plt.title("Number of hotels, restaurants and travelers in four regions in 2021")
plt.tight_layout()
plt.savefig("bar chart/png/425.png")
plt.clf()