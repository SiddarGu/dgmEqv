
import matplotlib.pyplot as plt 
import numpy as np

# create figure
plt.figure(figsize=(12,8))
# plot line chart
plt.plot(["USA","Canada","Mexico","Brazil"], 
         [2.5,1.8,1.3,0.9], 
         color="red", label="GDP growth(%)")
plt.plot(["USA","Canada","Mexico","Brazil"], 
         [3.6,6.2,4.6,12.5], 
         color="blue", label="Unemployment rate(%)")
plt.plot(["USA","Canada","Mexico","Brazil"], 
         [205.2,215.7,202.3,210.1], 
         color="green", label="Consumer Price Index(%)")
plt.plot(["USA","Canada","Mexico","Brazil"], 
         [2.2,1.5,3.4,4.3], 
         color="orange", label="Inflation rate(%)")

# set ticks
x_ticks = np.arange(0, 4, 1)
x_labels = ["USA","Canada","Mexico","Brazil"]
plt.xticks(x_ticks, x_labels, rotation=45)

# set legend and title
plt.title("Economic Performance in Major Latin American Countries in 2021")
plt.legend(loc="best", ncol=2, fontsize=15)
plt.tight_layout()
# save image
plt.savefig("line chart/png/190.png")

# clear current image state
plt.clf()