
import matplotlib.pyplot as plt
import numpy as np

#Define data
month = np.array(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
num_customers = np.array([200, 250, 300, 400, 350, 280, 250, 300, 320, 350, 400, 350]) 
avg_spending = np.array([100, 110, 160, 200, 180, 130, 120, 140, 150, 170, 200, 180]) 

#Create figure
fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot(111)

#Plot line chart
ax.plot(month, num_customers, label="Number of customers", marker='o')
ax.plot(month, avg_spending, label="Average spending(dollars)", marker='o')

#Set labels and legend
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Number of customers/Average spending(dollars)", fontsize=14)
ax.set_title("Monthly customer and spending trend in an e-commerce store", fontsize=16)
ax.legend(loc="best", fontsize=14)
ax.set_xticks(month)
ax.tick_params(labelsize=14)

#Adjust the length of label
plt.xticks(rotation=45)
plt.tight_layout()

#Save figure
plt.savefig("line chart/png/241.png")

#Clear figure
plt.clf()