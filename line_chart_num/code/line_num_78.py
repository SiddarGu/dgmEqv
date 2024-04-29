
import matplotlib.pyplot as plt 
plt.figure(figsize=(10, 6)) 
plt.subplot(111) 

year = [2010, 2011, 2012, 2013, 2014, 2015, 2016] 
smartphone_users = [100, 120, 140, 160, 180, 200, 220] 
tablet_users = [20, 30, 50, 60, 70, 80, 90] 
desktop_users = [50, 60, 70, 80, 90, 100, 110] 

plt.plot(year, smartphone_users, label="Smartphone Users") 
plt.plot(year, tablet_users, label="Tablet Users") 
plt.plot(year, desktop_users, label="Desktop Users") 

plt.xticks(year) 
plt.title("Number of users for different devices from 2010 to 2016") 
plt.xlabel("Year") 
plt.ylabel("Number of users (in millions)") 
plt.legend(loc="upper right") 

for index, data in enumerate(smartphone_users): 
    plt.annotate(str(data), xy=(year[index], data + 5)) 
for index, data in enumerate(tablet_users): 
    plt.annotate(str(data), xy=(year[index], data + 5)) 
for index, data in enumerate(desktop_users): 
    plt.annotate(str(data), xy=(year[index], data + 5)) 

plt.tight_layout() 
plt.savefig("line chart/png/240.png") 
plt.clf()