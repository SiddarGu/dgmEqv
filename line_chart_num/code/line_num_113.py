
import matplotlib.pyplot as plt
import matplotlib

#set figure size
plt.figure(figsize=(8,6))

#get data
data = [[2020,100,200,300],
        [2021,150,250,350], 
        [2022,200,300,400], 
        [2023,250,350,450]]

#draw line chart
plt.plot(data[0],data[1],label="Attendance at Concert A")
plt.plot(data[0],data[2],label="Attendance at Concert B")
plt.plot(data[0],data[3],label="Attendance at Concert C")

#add title
plt.title("Attendance at Three Concerts in a Four Year Period")

#add grid
plt.grid(True,linestyle="--")

#add labels
plt.xlabel("Year")
plt.ylabel("Attendance (thousand people)")

#add legend
plt.legend(loc="upper left")

#add ticks
plt.xticks(data[0])

#add labels for each data point
for x,y,z,w in data:
    plt.annotate(y,xy=(x,y))
    plt.annotate(z,xy=(x,z))
    plt.annotate(w,xy=(x,w))

#resize the image
plt.tight_layout()

#save the image
plt.savefig("line chart/png/171.png")

#clear the current image
plt.clf()