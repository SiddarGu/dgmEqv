
import matplotlib.pyplot as plt

#plot the data
data = [[2015, 50, 20, 10, 2], 
        [2016, 55, 25, 15, 3], 
        [2017, 60, 30, 20, 5], 
        [2018, 70, 35, 25, 8], 
        [2019, 75, 40, 30, 10]]

x = [i[0] for i in data]
y1 = [i[1] for i in data]
y2 = [i[2] for i in data]
y3 = [i[3] for i in data]
y4 = [i[4] for i in data]

plt.figure(figsize=(8,6))
plt.plot(x, y1, label="Smartphone Ownership(%)")
plt.plot(x, y2, label="Laptop Ownership(%)")
plt.plot(x, y3, label="Tablet Ownership(%)")
plt.plot(x, y4, label="Smart Speaker Ownership(%)")
plt.xticks(x)
plt.title("Global ownership of connected devices in 2015-2019")
plt.annotate("Smartphone Ownership(%)", xy=(2015, 50))
plt.annotate("Laptop Ownership(%)", xy=(2016, 25))
plt.annotate("Tablet Ownership(%)", xy=(2017, 20))
plt.annotate("Smart Speaker Ownership(%)", xy=(2018, 8))
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("line chart/png/196.png")
plt.clf()