
import matplotlib.pyplot as plt

x=[2001,2002,2003,2004,2005,2006,2007,2008]
House=[200,220,250,280,310,340,370,400]
Apartment=[100,120,140,160,180,200,220,240]

fig = plt.figure(figsize=(10,5))
plt.plot(x, House, color="red", linewidth=3, linestyle="-", label="House")
plt.plot(x, Apartment, color="blue", linewidth=3, linestyle="-", label="Apartment")

plt.title("Average housing prices in the US from 2001 to 2008")
plt.xlabel("Year")
plt.ylabel("Price (million dollars)")
plt.xticks(x, rotation=45, wrap=True)
plt.legend()
plt.tight_layout()

plt.savefig("line chart/png/543.png")
plt.clf()