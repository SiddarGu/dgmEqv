
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.plot([2015,2016,2017,2018,2019], [3,5,7,9,11], label="Organic Farming")
ax.plot([2015,2016,2017,2018,2019], [5,7,9,11,13], label="Crop Diversification")
ax.plot([2015,2016,2017,2018,2019], [1,2,3,4,5], label="Animal Husbandry")
ax.plot([2015,2016,2017,2018,2019], [2,4,6,8,10], label="Biodynamic Farming")
plt.xlabel("Year")
plt.ylabel("Rate of Adoption")
plt.title("Changes in Agricultural Practices in Europe from 2015-2019")
ax.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.xticks([2015,2016,2017,2018,2019]) 
plt.tight_layout()
plt.savefig("line chart/png/149.png")
plt.clf()