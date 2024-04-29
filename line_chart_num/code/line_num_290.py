
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,6))
year = np.array([2017,2018,2019,2020,2021])
a = np.array([1000,1100,1200,1300,1400])
b = np.array([1200,1100,1300,1400,1500])
c = np.array([800,900,1000,1100,1200])
plt.plot(year,a,label="Sales of Beverage A (million dollars)")
plt.plot(year,b,label="Sales of Beverage B (million dollars)")
plt.plot(year,c,label="Sales of Beverage C (million dollars)")
plt.title("Yearly Sales of Three Types of Beverages in the U.S. Food and Beverage Industry")
plt.xlabel("Year")
plt.ylabel("Sales (million dollars)")
plt.legend(loc="best")
plt.xticks(year)
for x,y in zip(year,a):
    plt.annotate(y,xy=(x,y),xytext=(-20,10),textcoords="offset points")
for x,y in zip(year,b):
    plt.annotate(y,xy=(x,y),xytext=(-20,10),textcoords="offset points")
for x,y in zip(year,c):
    plt.annotate(y,xy=(x,y),xytext=(-20,10),textcoords="offset points")
plt.tight_layout()
plt.savefig("line chart/png/126.png")
plt.clf()