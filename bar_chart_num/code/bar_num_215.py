
import matplotlib.pyplot as plt 

plt.figure(figsize=(8,5))
ax=plt.subplot()
plt.title("Number of Hotels and Tourists in four regions in 2021")

region = ["Americas", "Europe", "Asia", "Africa"]
hotels = [100, 150, 130, 90]
tourists = [20000, 25000, 24000, 19000]

x = [i for i,_ in enumerate(region)]

ax.bar(x, hotels, width=0.8, label="Hotels", color='b', bottom=0)
ax.bar(x, tourists, width=0.8, label="Tourists", color='r', bottom=hotels)

plt.xticks(x, region)

for i, v in enumerate(hotels):
    ax.text(i-0.15, v/2, str(v), color='white')
for i, v in enumerate(tourists):
    ax.text(i-0.15, hotels[i] + v/2, str(v), color='white')

plt.xlabel('Region')
plt.ylabel('Number')
plt.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/439.png')
plt.clf()