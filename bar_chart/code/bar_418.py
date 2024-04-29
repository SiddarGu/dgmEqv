
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot() 
ax.bar(["Football","Basketball","Hockey","Baseball"], 
       [75,20,12,30], width=0.6,bottom=0, color="green") 
ax.bar(["Football","Basketball","Hockey","Baseball"], 
       [7.5,2.5,1,3], width=0.6,bottom=0, color="red") 
plt.title("Average Attendance and Viewers for Four Sports in 2021", fontsize=14) 
ax.set_ylabel("Number", fontsize=14) 
ax.set_xticklabels(["Football","Basketball","Hockey","Baseball"], rotation=45, fontsize=14, wrap=True) 
ax.legend(["Average Attendance(thousand)", "Average Viewers(million)"], fontsize=12, loc="upper left") 
plt.tight_layout() 
fig.savefig("bar_418.png") 
plt.clf()