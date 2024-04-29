
import matplotlib.pyplot as plt 
import numpy as np 

plt.figure(figsize=(12, 8))
ax = plt.subplot()

year = np.array(["2000", "2001", "2002", "2003"])
painting = np.array([1000, 1200, 800, 1500])
sculpture = np.array([500, 600, 400, 800])
photography= np.array([200, 400, 100, 300])

plt.plot(year, painting, label="Painting")
plt.plot(year, sculpture, label="Sculpture")
plt.plot(year, photography, label="Photography")

plt.xticks(year, rotation=45, wrap=True)
ax.set_title("Revenues of art forms in the US from 2000 to 2003")
ax.legend(loc="best")

plt.grid(linestyle="--", alpha=0.8)
plt.tight_layout()
plt.savefig("line chart/png/99.png")
plt.clf()