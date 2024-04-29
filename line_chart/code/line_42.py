
import matplotlib.pyplot as plt

#create figure
plt.figure(figsize=(10,8))

#plot line chart
x = [2000, 2001, 2002, 2003, 2004]
y1 = [100, 120, 110, 90, 140]
y2 = [80, 75, 90, 105, 110]
y3 = [150, 155, 140, 160, 145]

plt.plot(x, y1, marker='o', label="Number of Music Albums Released")
plt.plot(x, y2, marker='o', label="Number of Movies Released")
plt.plot(x, y3, marker='o', label="Number of Books Released")

#set xticks
plt.xticks(x)

#add title
plt.title("Number of Artistic Works Released in the US from 2000 to 2004")

#add legend
plt.legend(loc="upper right")

#resize the image
plt.tight_layout()

#save the image
plt.savefig("line chart/png/531.png")

#clear the current image state
plt.clf()