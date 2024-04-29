
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5))

x = np.array([2016,2017,2018,2019,2020])
emps = np.array([50,60,75,100,120])
vdays = np.array([2,3,4,5,6])

plt.plot(x, emps, label="Employees")
plt.plot(x, vdays, label="Vacation Days")
plt.xticks(x)

plt.title("Increase of Employees and Vacation Days in a Company from 2016 to 2020")
plt.xlabel("Year")
plt.ylabel("Number")
plt.legend(loc="upper left")

plt.tight_layout()

plt.savefig("line chart/png/89.png")

plt.clf()