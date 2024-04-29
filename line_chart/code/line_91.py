
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
x = [2001,2002,2003,2004]
y1 = [500,700,900,1100]
y2 = [400,600,800,1000]
y3 = [600,800,1000,1200]
plt.plot(x, y1, label="Painting")
plt.plot(x, y2, label="Sculpture")
plt.plot(x, y3, label="Photography")
plt.title("Art pieces created in four art forms from 2001 to 2004")
plt.xticks(x)
plt.xlabel("Year")
plt.ylabel("Number")
plt.legend(loc='best')
plt.grid(True, linestyle='--', color='gray', alpha=0.5)
plt.tight_layout()
plt.savefig("line chart/png/88.png")
plt.clf()