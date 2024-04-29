
import matplotlib.pyplot as plt
import numpy as np

Month = ["January","February","March","April","May","June"]
Part_A = [500,600,700,800,1000,1200]
Part_B = [1000,1200,1400,1600,1400,1600]
Part_C = [1500,1400,1600,1800,2000,2200]

fig, ax = plt.subplots(figsize=(15,10))
ax.plot(Month,Part_A,label="Part A",marker="o")
ax.plot(Month,Part_B,label="Part B",marker="o")
ax.plot(Month,Part_C,label="Part C",marker="o")
ax.set_title("Production level of three parts in a car manufacturing plant over six months")
ax.set_xlabel("Month")
ax.set_ylabel("Production Level")
ax.legend(loc=2)

# set x ticks to prevent interpolation
x = np.arange(0,6,1)
ticks = [Month[i] for i in x]
plt.xticks(x,ticks)

# adjust figure and save
plt.tight_layout()
plt.savefig("line chart/png/57.png")

# Clear the current image state
plt.clf()