

import matplotlib.pyplot as plt
import numpy as np

month= ["January", "February", "March", "April", "May", "June", "July", "August"]
donations_A = [100,110,120,130,140,150,160,170]
donations_B = [50,60,70,80,90,100,110,120]
donations_C = [20,30,40,50,60,70,80,90]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
plt.plot(month,donations_A, label="Donations A (million dollars)", marker='o', color='blue')
plt.plot(month,donations_B, label="Donations B (million dollars)", marker='o', color='green')
plt.plot(month,donations_C, label="Donations C (million dollars)", marker='o', color='red')
plt.xlabel("Month")
plt.ylabel("Donations (million dollars)")
plt.title("Monthly donations to three charities in 2020")
plt.xticks(np.arange(len(month)),month, rotation=45, wrap=True)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),  shadow=True, ncol=3)
for i,j in zip(month, donations_A):
    ax.annotate(str(j),xy=(i,j+4))
for i,j in zip(month, donations_B):
    ax.annotate(str(j),xy=(i,j+4))
for i,j in zip(month, donations_C):
    ax.annotate(str(j),xy=(i,j+4))
fig.tight_layout()
plt.savefig("line chart/png/569.png")
plt.clf()