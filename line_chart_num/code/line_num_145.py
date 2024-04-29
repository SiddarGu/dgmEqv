
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15,8)) 
x = np.array([2000,2001,2002,2003,2004])
web_users = np.array([200,250,300,350,400])
smartphone_users = np.array([0,10,25,50,80])
computer_users = np.array([100,130,150,170,200])

plt.plot(x, web_users, label="Web Users")
plt.plot(x, smartphone_users, label="Smartphone Users")
plt.plot(x, computer_users, label="Computer Users")

plt.title("Global Technology Usage from 2000 to 2004")
plt.xlabel("Year")
plt.ylabel("Users (millions)")
plt.xticks(x)

for a,b,c in zip(x,web_users,computer_users):
    plt.annotate("({},{})".format(a,b), xy=(a,b), xytext=(a-0.2, b+20))
    plt.annotate("({},{})".format(a,c), xy=(a,c), xytext=(a-0.2, c+10))

plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("line chart/png/486.png")
plt.clf()