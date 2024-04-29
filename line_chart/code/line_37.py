
import matplotlib.pyplot as plt
import numpy as np

#Set the size of the figure
plt.figure(figsize=(8,5))

#Generate chart
ax = plt.subplot()
x = np.arange(18,26)
y = [35000,30000,40000,38000,42000,45000,50000,47000]
plt.plot(x, y, color='orange', marker='o', linestyle='--', label="Average Salary")

#Set title of the figure
plt.title("Average Salary of 18-25 Year Olds in the US in 2021")

#Set x-axis and y-axis
plt.xlabel("Age")
plt.ylabel("Average Salary(USD)")

#Set the x-axis ticks
plt.xticks(x)

#Add legend
plt.legend(loc='best')

#Add background grid
plt.grid()

#Resize the image
plt.tight_layout()

#Save figure
plt.savefig("line chart/png/312.png")

#Clear the current image state
plt.cla()
plt.clf()
plt.close()