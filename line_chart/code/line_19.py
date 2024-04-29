
import matplotlib.pyplot as plt
import numpy as np

data = [[2015,100,80,120,150],
        [2016,120,90,110,160],
        [2017,80,110,130,120],
        [2018,150,120,140,80]]

year, donations_A, donations_B, donations_C, donations_D = np.array(data).T

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(year, donations_A, label="Donations A(million dollars)")
ax.plot(year, donations_B, label="Donations B(million dollars)")
ax.plot(year, donations_C, label="Donations C(million dollars)")
ax.plot(year, donations_D, label="Donations D(million dollars)")
ax.set_xticks(year)
ax.set_xticklabels(year, rotation=30, ha="right")
ax.set_title("Donations to Four Nonprofit Organizations in the Past Four Years")
ax.legend(loc="best")
plt.tight_layout()
plt.savefig("line chart/png/320.png")
plt.clf()