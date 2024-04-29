
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15, 8))

x = np.array([2019, 2020, 2021, 2022])
A = np.array([200, 250, 300, 400])
B = np.array([100, 150, 200, 250])
C = np.array([400, 500, 350, 450])
D = np.array([350, 300, 400, 350])

plt.plot(x, A, label="Movie Box Office A")
plt.plot(x, B, label="Movie Box Office B")
plt.plot(x, C, label="Movie Box Office C")
plt.plot(x, D, label="Movie Box Office D")

plt.title("Movie Box Office earnings of four films in USA from 2019 to 2022")
plt.xlabel("Year")
plt.ylabel("Movie Box Office (million dollars)")
plt.grid(True)
plt.xticks(x)
plt.legend(loc="best", ncol=2, fontsize="large", frameon=True)
plt.tight_layout()
plt.savefig("line chart/png/123.png")
plt.clf()