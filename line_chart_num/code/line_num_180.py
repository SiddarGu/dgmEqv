
import matplotlib.pyplot as plt 

plt.figure(figsize=(13, 9)) 
ax = plt.subplot() 

xdata = [2001, 2002, 2003, 2004, 2005] 
ydata1 = [1000, 1200, 900, 1100, 1500] 
ydata2 = [500, 400, 450, 600, 700] 

ax.plot(xdata, ydata1, label='Donations(million dollars)', color='green') 
ax.plot(xdata, ydata2, label='Volunteer Hours', color='red') 

for i, j in zip(xdata, ydata1): 
    ax.annotate(str(j), xy=(i, j)) 

for i, j in zip(xdata, ydata2): 
    ax.annotate(str(j), xy=(i, j)) 

ax.set_title('Donation and Volunteer Hours Contributed to Nonprofit Organizations in the US from 2001 to 2005') 
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), 
          ncol=2, fontsize='large') 
plt.xticks(xdata) 
plt.tight_layout() 
plt.savefig('line chart/png/192.png') 
plt.clf()