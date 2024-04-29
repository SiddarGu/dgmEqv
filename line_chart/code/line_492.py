
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(["2001","2002","2003","2004"],[500000,700000,800000,650000],label="Internet Users")
plt.plot(["2001","2002","2003","2004"],[4000000,5000000,5500000,6000000],label="Phone Users")
plt.plot(["2001","2002","2003","2004"],[3000000,3500000,4000000,4500000],label="Computer Users")
plt.xticks(["2001","2002","2003","2004"])
plt.title("Global Usage of Technology in 2001-2004")
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("line chart/png/63.png")
plt.clf()