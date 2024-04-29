
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,5))
x = np.array([20,25,30,35,40,45,50,55])
y = np.array([200,150,120,100,80,60,40,30])
plt.plot(x,y,label="Viscosity",linestyle="-",marker="o")
plt.title("Viscosity of a substance at different temperatures")
plt.xlabel("Temperature (degrees Celsius)")
plt.ylabel("Viscosity (cP)")
plt.xticks(x)
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("line chart/png/371.png")
plt.clf()