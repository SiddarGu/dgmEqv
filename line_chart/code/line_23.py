
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
x=['March','April','May','June','July','August','September']
y1=[1000,1100,1300,1400,1600,1800,1500]
y2=[1200,1300,1500,1700,1800,2000,1800]
y3=[1500,1400,1700,1900,2100,2200,2400]
plt.plot(x,y1,color='blue',label="Wheat Production")
plt.plot(x,y2,color='red',label="Rice Production")
plt.plot(x,y3,color='green',label="Corn Production")
plt.xticks(rotation=45)
plt.title("Crop Production in the Midwest United States from March to September")
plt.xlabel("Month")
plt.ylabel("Production")
plt.legend(loc="best", prop={'size': 8}, bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig('line chart/png/60.png')
plt.clf()