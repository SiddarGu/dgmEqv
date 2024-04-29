
import matplotlib.pyplot as plt
import numpy as np

#create figure
fig = plt.figure(figsize=(12, 8)) 

#prepare data
modes = ["Air Travel", "Rail Travel", "Road Transport", "Water Transport", "Other"]
percentage = [25, 15, 35, 15, 10]

#plot data
ax = fig.add_subplot(111)
wedges, texts, autotexts = ax.pie(percentage, labels=modes,
                                  autopct="%1.2f%%",
                                  startangle=90,
                                  shadow=True,
                                  rotatelabels=True,
                                  radius=1.5,
                                  wedgeprops={"linewidth":2,
                                              "edgecolor":"black"})

#modify text
for t in texts:
    t.set_wrap(True)
plt.setp(autotexts, size=13, weight="bold")

#set title
ax.set_title("Distribution of Different Modes of Transport in the USA, 2023", fontsize=20)

#resize image
plt.tight_layout()

#save figure
plt.savefig("pie chart/png/419.png")

#clear image state
plt.clf()