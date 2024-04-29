
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))

x = np.arange(2001, 2007)
y1 = np.array([78, 79, 80, 82, 84, 85])
y2 = np.array([72, 74, 76, 78, 80, 81])

plt.plot(x, y1, label="Enrollment Rate(%)")
plt.plot(x, y2, label="Graduation Rate(%)")

plt.title("Educational Enrollment and Graduation Rates in the U.S. from 2001 to 2006")
plt.xlabel("Year")
plt.ylabel("Rate(%)")

plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='0.8')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='0.9')

plt.legend(fontsize=8)

for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=8)
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='top', fontsize=8)

plt.xticks(x, x, rotation=45)

plt.tight_layout()
plt.savefig("line chart/png/355.png", dpi=300)
plt.clf()