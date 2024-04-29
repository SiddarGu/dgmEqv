
import matplotlib.pyplot as plt
import numpy as np

#data
year = [2014,2015,2016,2017,2018]
Facebook_Users = [1200,1700,2500,3500,4500]
Google_Searches = [200,220,250,290,320]
Twitter_Users = [90,110,150,200,240]
Pinterest_Users = [20,50,80,100,150]

#plot
fig=plt.figure(figsize=(8,5))
plt.plot(year,Facebook_Users,label="Facebook Users(million)")
plt.plot(year,Google_Searches,label="Google Searches(million)")
plt.plot(year,Twitter_Users,label="Twitter Users(million)")
plt.plot(year,Pinterest_Users,label="Pinterest Users(million)")
plt.xticks(year)
plt.title("Increase in Social Media Usage from 2014 to 2018")
plt.xlabel("year")
plt.ylabel("Number of Users(million)")
plt.legend()
plt.grid(True)

#annotate
plt.annotate("Facebook : {}".format(Facebook_Users[4]),xy=(2018,4500),xytext=(2015,3000),arrowprops=dict(facecolor='black',shrink=0.05))
plt.annotate("Google : {}".format(Google_Searches[4]),xy=(2018,320),xytext=(2015,220),arrowprops=dict(facecolor='black',shrink=0.05))
plt.annotate("Twitter : {}".format(Twitter_Users[4]),xy=(2018,240),xytext=(2015,150),arrowprops=dict(facecolor='black',shrink=0.05))
plt.annotate("Pinterest : {}".format(Pinterest_Users[4]),xy=(2018,150),xytext=(2015,50),arrowprops=dict(facecolor='black',shrink=0.05))

#save image
plt.tight_layout()
plt.savefig('line chart/png/200.png')

#clear current image state
plt.clf()