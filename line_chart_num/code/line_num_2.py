
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

Month = ["January","February","March","April","May","June","July","August"]
Number_of_Tourists = [2.3,2.4,2.8,3.2,3.5,3.8,4.2,4.5]
Number_of_Hotels = [10,11,12,13,15,17,19,22]

plt.figure(figsize=(10,8))
plt.plot(Month,Number_of_Tourists,color = 'r',label="Number of Tourists (million)")
plt.plot(Month,Number_of_Hotels,color = 'g',label="Number of Hotels")

#add grids
plt.grid(linestyle='-.')

#add title and font
plt.title("Global Tourists and Hotel Capacity Increase from January to August 2023", fontsize=14)

#add x and y axis names
plt.xlabel("Month", fontsize=13)
plt.ylabel("Number", fontsize=13)

#add xticks
plt.xticks(np.arange(len(Month)),Month)

#add legend
plt.legend(loc="best", fontsize=12)

#add annotation
for a,b in zip(Month,Number_of_Tourists):
    plt.text(a, b+0.1, '%.1f' % b, ha='center', va= 'bottom',fontsize=9)

for a,b in zip(Month,Number_of_Hotels):
    plt.text(a, b+0.1, '%.1f' % b, ha='center', va= 'bottom',fontsize=9)

#automatically resize the image
plt.tight_layout()

#save the image
plt.savefig("line chart/png/27.png")

#clear the current image state
plt.clf()