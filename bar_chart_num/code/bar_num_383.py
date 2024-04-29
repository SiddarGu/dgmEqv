
import matplotlib.pyplot as plt 
import numpy as np 

#Data 
Company=['Amazon','Walmart','Target','Costco'] 
Online_Sales=[90,80,55,60] 
Store_Sales=[60,70,45,50] 

#Create figure 
fig, ax = plt.subplots(figsize=(10,7)) 

#Plotting the bars 
ax.bar(Company,Online_Sales, label="Online Sales", bottom=Store_Sales, color='r', width=0.5) 
ax.bar(Company,Store_Sales, label="Store Sales", color='b', width=0.5) 

#Adding the legend and title 
ax.legend(loc="upper right") 
ax.set_title("Total sales of four companies in 2021") 

#Adding the xticks 
ax.set_xticks(np.arange(len(Company))) 
ax.set_xticklabels(Company)

#Labeling the bars 
for x,y1,y2 in zip(Company,Online_Sales,Store_Sales): 
    ax.text(x, y1 + y2/2, '{}'.format(y1), ha="center", va="center", fontsize=13) 
    ax.text(x, y2/2, '{}'.format(y2), ha="center", va="center", fontsize=13) 

#Saving the figure 
plt.tight_layout() 
plt.savefig("Bar Chart/png/237.png") 
plt.clf()