
import matplotlib.pyplot as plt 
import numpy as np 

data = np.array([[600,800],[500,700],[400,600],[350,500]])
Organization = ["Red Cross", "Unicef", "Salvation Army", "World Vision"]

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(Organization, data[:,0], label="Funds Raised", color="red")
ax.bar(Organization, data[:,1], label="Donations", color="blue", bottom=data[:,0])
ax.set_title("Funds raised and donations of four nonprofit organizations in 2021")
ax.set_xticks(Organization)
ax.set_ylabel("million")
ax.legend(loc="upper left")

for i in range(len(Organization)):
    ax.text(x=i-0.25, y=data[i,0]+data[i,1]/2, s=data[i,0]+data[i,1], rotation=90, wrap=True, fontsize=10)

fig.tight_layout()
plt.savefig("Bar Chart/png/111.png")
plt.clf()