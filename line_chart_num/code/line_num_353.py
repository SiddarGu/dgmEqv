
import matplotlib.pyplot as plt
import numpy as np

data=[[1800,10,15,20,25],[1810,15,17,20,30],[1820,20,18,25,35],[1830,25,20,30,40]]

X=np.array([x[0] for x in data])
A=np.array([x[1] for x in data])
B=np.array([x[2] for x in data])
C=np.array([x[3] for x in data])
D=np.array([x[4] for x in data])

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(1,1,1)
ax.plot(X,A, label="Painting A")
ax.plot(X,B, label="Painting B")
ax.plot(X,C, label="Painting C")
ax.plot(X,D, label="Painting D")
ax.set_title("Number of Paintings in Different Art Galleries from 1800 to 1830")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Paintings")
ax.legend(loc='best')
for i in range(len(data)):
    ax.annotate(data[i][1:],xy=(X[i],A[i]), xytext=(-20,10), textcoords="offset points", fontsize=12)
plt.xticks(X)
plt.tight_layout()
plt.savefig("line chart/png/262.png")
plt.clf()