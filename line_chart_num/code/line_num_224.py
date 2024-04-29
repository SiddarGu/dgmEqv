
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False

year = np.array([2000,2001,2002,2003,2004])
criminal_cases = np.array([1000,1500,1200,1000,1300])
civil_cases = np.array([2000,2500,3000,3500,4000])
family_cases = np.array([500,800,700,900,1200])

plt.figure(figsize=(8,4))
ax = plt.subplot()
ax.plot(year,criminal_cases,label="Criminal Cases")
ax.plot(year,civil_cases,label="Civil Cases")
ax.plot(year,family_cases,label="Family Cases")

plt.title("Cases reported in US court system in 2000-2004")
plt.xlabel("Year")
plt.ylabel("Cases")
plt.xticks(year,rotation=30)

ax.annotate('Criminal Cases:1000',xy=(2000,1000),xytext=(2000,2500),
            arrowprops=dict(facecolor='black',shrink=0.05))
ax.annotate('Civil Cases:2000',xy=(2000,2000),xytext=(2000,3000),
            arrowprops=dict(facecolor='black',shrink=0.05))
ax.annotate('Family Cases:500',xy=(2000,500),xytext=(2000,1000),
            arrowprops=dict(facecolor='black',shrink=0.05))

plt.legend(loc="best")
plt.grid()
plt.tight_layout()

plt.savefig("line chart/png/277.png")
plt.clf()