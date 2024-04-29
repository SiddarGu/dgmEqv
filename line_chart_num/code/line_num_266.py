
import matplotlib.pyplot as plt
import numpy as np

#create figure
plt.figure(figsize=(8,4))
ax=plt.subplot()

#data
x = np.array(["2008","2012","2016","2020"])
y1 = np.array([50,52,55,58])
y2 = np.array([45,47,44,41])
y3 = np.array([2,1,1,1])

#plot line
ax.plot(x, y1, label="Party A(millions)")
ax.plot(x, y2, label="Party B(millions)")
ax.plot(x, y3, label="Party C(millions)")

#title
plt.title("Electoral Results in the United States from 2008 to 2020", fontsize=18)

#xticks
plt.xticks(x, fontsize=15)

#label
for a, b, c in zip(x,y1,y2):
    ax.annotate(str(b)+","+str(c), xy=(a,b), xytext=(-15,5), textcoords='offset points', fontsize=15)

#legend
plt.legend(loc="upper left", fontsize=15)

#save
plt.savefig('line chart/png/252.png', dpi=300)

#clear
plt.clf()