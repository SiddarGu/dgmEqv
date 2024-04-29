
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6))
ax=plt.subplot()

Year = [2001, 2002, 2003, 2004]
Expenses_A = [100, 120, 80, 150]
Expenses_B = [80, 90, 110, 120]
Expenses_C = [120, 110, 130, 140]
Expenses_D = [150, 160, 120, 80]

ax.plot(Year, Expenses_A, label="Expenses A (million dollars)", marker='o')
ax.plot(Year, Expenses_B, label="Expenses B (million dollars)", marker='o')
ax.plot(Year, Expenses_C, label="Expenses C (million dollars)", marker='o')
ax.plot(Year, Expenses_D, label="Expenses D (million dollars)", marker='o')

plt.xticks(Year, Year, rotation=45)
plt.xlabel("Year")
plt.ylabel("Expenses (million dollars)")
plt.title("Expenses in four categories of products")
plt.legend(loc="best")

for a,b in zip(Year, Expenses_A):
    ax.annotate("{}".format(b), xy=(a,b), xytext=(a-0.20,b+0.20), fontsize=8)
for a,b in zip(Year, Expenses_B):
    ax.annotate("{}".format(b), xy=(a,b), xytext=(a-0.20,b+0.20), fontsize=8)
for a,b in zip(Year, Expenses_C):
    ax.annotate("{}".format(b), xy=(a,b), xytext=(a-0.20,b+0.20), fontsize=8)
for a,b in zip(Year, Expenses_D):
    ax.annotate("{}".format(b), xy=(a,b), xytext=(a-0.20,b+0.20), fontsize=8)
    
plt.tight_layout()
plt.savefig("line chart/png/255.png")
plt.clf()