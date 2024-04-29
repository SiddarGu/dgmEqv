
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(8,5)) 
plt.title("Average home prices and sizes in four major US cities in 2021") 
ax = fig.add_subplot() 
ax.set_xlabel("City") 
ax.set_ylabel("Average Home Prices/sq ft") 
plt.xticks(rotation=45, ha="right") 
ax.bar(["New York", "Los Angeles", "Chicago", "Houston"], 
        [800000, 700000, 600000, 500000], 
        width=0.5, label="Average Home Prices", 
        color="r", bottom=0) 
ax.bar(["New York", "Los Angeles", "Chicago", "Houston"], 
        [2500, 2100, 1800, 1500], 
        width=0.5, label="Average Home Size (sq ft)", 
        color="b", bottom=[800000, 700000, 600000, 500000]) 
ax.legend(loc="best") 
plt.tight_layout() 
plt.savefig('bar chart/png/366.png') 
plt.clf()