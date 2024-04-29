
import matplotlib.pyplot as plt
import numpy as np

x_labels = ["January","February","March","April","May"]
y_Tweets = [20000,25000,30000,35000,40000]
y_Instagram = [30000,35000,40000,45000,50000]
y_Facebook = [40000,45000,50000,55000,60000]

fig = plt.figure(figsize=(10,6))

plt.plot(x_labels, y_Tweets, linestyle="-", marker="o", color="b", label="Tweets")
plt.plot(x_labels, y_Instagram, linestyle="-", marker="o", color="r", label="Instagram")
plt.plot(x_labels, y_Facebook, linestyle="-", marker="o", color="g", label="Facebook")

plt.title("Increase in Social Media Posts from January to May 2021")
plt.xlabel("Month")
plt.ylabel("Number of Posts")
plt.xticks(np.arange(len(x_labels)), x_labels)
plt.legend(loc="best")

plt.tight_layout()
plt.savefig("line chart/png/236.png")
plt.clf()